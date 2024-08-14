from pathlib import Path
from audio_extract import extract_audio
from typing import List, Dict
import logging
import whisper
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_excluded(file_path: Path, exclude: List[str]) -> bool:
    """Check if the file or its parent directories are in the exclude list."""
    return any(ex in file_path.parts for ex in exclude) or file_path.name in exclude

def extract_audio_from_file(video_file: Path) -> Path:
    """Extract audio from a video file and return the path to the audio file."""
    audio_output_path = video_file.with_name(f"{video_file.stem}_audio.mp3")
    extract_audio(input_path=str(video_file), output_path=str(audio_output_path), overwrite=True)
    logging.info(f"Extracted audio from {video_file} to {audio_output_path}")
    return audio_output_path

def transcribe_audio(audio_file: Path, model) -> Dict:
    """Transcribe audio using the Whisper model and return the transcription result."""
    result = model.transcribe(str(audio_file))
    logging.info(f"Transcribed audio from {audio_file}")
    return result

def save_transcription(transcript: Dict, transcript_output_path: Path) -> None:
    """Save transcription result to a JSON file and the text to a .txt file."""
    # Save transcription to JSON file
    with open(transcript_output_path, 'w') as transcript_file:
        json.dump(transcript, transcript_file, ensure_ascii=False, indent=4)
    logging.info(f"Saved transcription to {transcript_output_path}")

    # Extract text and save to a .txt file
    text_output_path = transcript_output_path.with_suffix('.txt')
    with open(text_output_path, 'w') as text_file:
        text_file.write(transcript.get('text', ''))
    logging.info(f"Saved transcribed text to {text_output_path}")

def process_video_file(video_file: Path, model) -> None:
    """Process a single video file: extract audio, transcribe it, and save the results."""
    try:
        audio_file = extract_audio_from_file(video_file)
        transcript = transcribe_audio(audio_file, model)
        transcript_output_path = video_file.with_name(f"{video_file.stem}_whisper_transcript.json")
        save_transcription(transcript, transcript_output_path)
    except Exception as e:
        logging.error(f"Failed to process {video_file}: {e}")

def extract_audio_from_videos(directory: str,
                               exclude: List[str] = None,
                                 whisper_model: str = "base"
                               ) -> None:
    """
    Recursively searches for .mp4 files (case-insensitive) in the specified directory,
    extracts their audio, transcribes it, and saves the results as .mp3 and .json files.

    Parameters
    ----------
    directory : str
        The directory to search for video files.
    exclude : List[str], optional
        List of file or folder names to exclude from processing.

    Examples
    --------
    >>> extract_audio_from_videos('/path/to/directory', exclude=['exclude_folder', 'exclude_file.mp4'], whisper_model='large')
    """
    if exclude is None:
        exclude = []

    path = Path(directory)
    model = whisper.load_model(whisper_model)

    logging.info(f"Starting audio extraction and transcription in directory: {directory}")
    for video_file in path.rglob('*'):
        if is_excluded(video_file, exclude):
            logging.info(f"Skipping excluded file or folder: {video_file}")
            continue
        if video_file.suffix.lower() == '.mp4':
            process_video_file(video_file, model)

    logging.info("Audio extraction and transcription completed.")

if __name__ == "__main__":
    directory = r"D:\videos\obs-recordings\2024-08-09"
    exclude = ['exclude_folder', 'exclude_file.mp4']
    whisper_model = "large" # use `base.en` if you're in a hurry and only speaking english, but the results are noticably better with the `large` model
    extract_audio_from_videos(directory=directory, exclude=exclude, whisper_model=whisper_model)
