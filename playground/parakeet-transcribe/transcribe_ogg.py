#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "transformers>=4.46",
##     "torch",
#     "torch",
#     "soundfile",
#     "scipy",
#     "accelerate",
#"librosa"
# ]
# ///
"""Transcribe an .ogg audio file using NVIDIA Parakeet CTC via HuggingFace Transformers.

Saves output as:
- {filename}_transcript.txt (raw text)
- {filename}_transcript.md (formatted markdown with stats)
- {filename}_transcript.json (verbose JSON with all metadata)
"""

import json
from datetime import datetime
from pathlib import Path
from time import perf_counter

import numpy as np
import soundfile as sf
import torch
from numpy.typing import NDArray
from scipy.signal import resample_poly
from transformers import AutoModelForCTC, AutoProcessor

# ============================================================
# CONFIGURE THIS PATH
# ============================================================
INPUT_OGG_PATH = Path("./voice-message.ogg")
# ============================================================

TARGET_SAMPLE_RATE = 16000
MODEL_NAME = "nvidia/parakeet-ctc-1.1b"

CHUNK_DURATION_SECS = 25.0
OVERLAP_SECS = 2.0


def load_and_resample_ogg(ogg_path: Path) -> tuple[NDArray[np.float32], int]:
    """Load an OGG file and resample to 16kHz mono. Returns (audio_data, original_sample_rate)."""
    data, sample_rate = sf.read(ogg_path, dtype="float32")
    original_sample_rate = sample_rate

    if data.ndim == 2:
        data = np.mean(data, axis=1)

    if sample_rate != TARGET_SAMPLE_RATE:
        gcd = np.gcd(TARGET_SAMPLE_RATE, sample_rate)
        up = TARGET_SAMPLE_RATE // gcd
        down = sample_rate // gcd
        data = resample_poly(data, up, down).astype(np.float32)

    return data, original_sample_rate


def chunk_audio(
    audio: NDArray[np.float32],
    sample_rate: int,
    chunk_secs: float,
    overlap_secs: float,
) -> list[NDArray[np.float32]]:
    """Split audio into overlapping chunks."""
    chunk_samples = int(chunk_secs * sample_rate)
    overlap_samples = int(overlap_secs * sample_rate)
    step = chunk_samples - overlap_samples

    chunks: list[NDArray[np.float32]] = []
    start = 0

    while start < len(audio):
        end = min(start + chunk_samples, len(audio))
        chunks.append(audio[start:end])
        start += step

        if len(audio) - start < overlap_samples:
            break

    return chunks


def transcribe(ogg_path: Path) -> dict:
    """Transcribe an OGG file and return full results dict."""
    if not ogg_path.exists():
        raise FileNotFoundError(f"File not found: {ogg_path}")

    if ogg_path.suffix.lower() != ".ogg":
        raise ValueError(f"Expected .ogg file, got: {ogg_path.suffix}")

    start_time = perf_counter()

    print(f"Loading and resampling: {ogg_path.name}")
    audio_data, original_sample_rate = load_and_resample_ogg(ogg_path)

    duration_secs = len(audio_data) / TARGET_SAMPLE_RATE
    print(f"Audio duration: {duration_secs:.1f} seconds")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    print(f"Loading model: {MODEL_NAME}")
    processor = AutoProcessor.from_pretrained(MODEL_NAME)
    model = AutoModelForCTC.from_pretrained(MODEL_NAME, torch_dtype="auto")
    model = model.to(device)

    model_load_time = perf_counter() - start_time

    if duration_secs > CHUNK_DURATION_SECS:
        chunks = chunk_audio(
            audio_data,
            TARGET_SAMPLE_RATE,
            CHUNK_DURATION_SECS,
            OVERLAP_SECS,
        )
        print(f"Split into {len(chunks)} chunks")
    else:
        chunks = [audio_data]

    chunk_transcripts: list[dict] = []
    inference_start = perf_counter()

    for i, chunk in enumerate(chunks):
        chunk_start_time = perf_counter()

        if len(chunks) > 1:
            print(f"Transcribing chunk {i + 1}/{len(chunks)}...")

        inputs = processor(
            chunk,
            sampling_rate=TARGET_SAMPLE_RATE,
            return_tensors="pt",
        )
        inputs = inputs.to(device=device, dtype=model.dtype)

        with torch.no_grad():
            outputs = model.generate(**inputs)

        chunk_text = processor.batch_decode(outputs)[0]
        chunk_duration = len(chunk) / TARGET_SAMPLE_RATE

        chunk_transcripts.append({
            "chunk_index": i,
            "text": chunk_text,
            "chunk_duration_secs": round(chunk_duration, 2),
            "processing_time_secs": round(perf_counter() - chunk_start_time, 2),
        })

    inference_time = perf_counter() - inference_start
    total_time = perf_counter() - start_time

    full_transcript = " ".join(ct["text"] for ct in chunk_transcripts)

    word_count = len(full_transcript.split())
    char_count = len(full_transcript)

    results = {
        "transcript": full_transcript,
        "metadata": {
            "source_file": str(ogg_path.resolve()),
            "source_filename": ogg_path.name,
            "timestamp": datetime.now().isoformat(),
            "model": MODEL_NAME,
            "device": device,
        },
        "audio_info": {
            "duration_secs": round(duration_secs, 2),
            "original_sample_rate": original_sample_rate,
            "target_sample_rate": TARGET_SAMPLE_RATE,
            "num_chunks": len(chunks),
            "chunk_duration_secs": CHUNK_DURATION_SECS,
            "overlap_secs": OVERLAP_SECS,
        },
        "transcript_stats": {
            "word_count": word_count,
            "character_count": char_count,
            "words_per_minute": round(word_count / (duration_secs / 60), 1) if duration_secs > 0 else 0,
        },
        "timing": {
            "model_load_time_secs": round(model_load_time, 2),
            "inference_time_secs": round(inference_time, 2),
            "total_time_secs": round(total_time, 2),
            "realtime_factor": round(duration_secs / inference_time, 2) if inference_time > 0 else 0,
        },
        "chunks": chunk_transcripts,
    }

    return results


def save_outputs(results: dict, output_dir: Path) -> dict[str, Path]:
    """Save transcript in txt, markdown, and json formats."""
    base_name = Path(results["metadata"]["source_filename"]).stem

    # Paths
    txt_path = output_dir / f"{base_name}_transcript.txt"
    md_path = output_dir / f"{base_name}_transcript.md"
    json_path = output_dir / f"{base_name}_transcript.json"

    # 1. Raw text
    txt_path.write_text(results["transcript"], encoding="utf-8")
    print(f"Saved: {txt_path}")

    # 2. Formatted Markdown
    md_content = f"""# Transcript: {results["metadata"]["source_filename"]}

## Summary

| Metric | Value |
|--------|-------|
| Duration | {results["audio_info"]["duration_secs"]} seconds ({results["audio_info"]["duration_secs"]/60:.1f} minutes) |
| Word Count | {results["transcript_stats"]["word_count"]} |
| Words/Minute | {results["transcript_stats"]["words_per_minute"]} |
| Processing Time | {results["timing"]["total_time_secs"]} seconds |
| Realtime Factor | {results["timing"]["realtime_factor"]}x |

## Details

- **Model:** {results["metadata"]["model"]}
- **Device:** {results["metadata"]["device"]}
- **Timestamp:** {results["metadata"]["timestamp"]}
- **Chunks:** {results["audio_info"]["num_chunks"]}

---

## Transcript

{results["transcript"]}

---

## Chunk Details

"""
    for chunk in results["chunks"]:
        md_content += f"""### Chunk {chunk["chunk_index"] + 1}

- Duration: {chunk["chunk_duration_secs"]}s
- Processing time: {chunk["processing_time_secs"]}s

> {chunk["text"]}

"""

    md_path.write_text(md_content, encoding="utf-8")
    print(f"Saved: {md_path}")

    # 3. Verbose JSON
    json_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved: {json_path}")

    return {
        "txt": txt_path,
        "md": md_path,
        "json": json_path,
    }


def main() -> None:
    results = transcribe(INPUT_OGG_PATH)
    output_dir = INPUT_OGG_PATH.parent

    print("\n" + "=" * 50)
    print("TRANSCRIPT")
    print("=" * 50)
    print(results["transcript"])
    print("=" * 50)

    print(f"\nStats:")
    print(f"  Duration: {results['audio_info']['duration_secs']}s")
    print(f"  Words: {results['transcript_stats']['word_count']}")
    print(f"  Processing: {results['timing']['total_time_secs']}s")
    print(f"  Realtime factor: {results['timing']['realtime_factor']}x")

    print(f"\nSaving outputs to: {output_dir}")
    saved = save_outputs(results, output_dir)

    print("\n✓ Done!")


if __name__ == "__main__":
    main()