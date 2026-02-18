# Whisper Transcriber — Tauri v2 + whisper.cpp Local STT

A standalone desktop app that captures your microphone, runs local Whisper transcription via `whisper-rs` (whisper.cpp bindings), displays a live waveform, and feeds transcribed text into a Monaco editor.

---

## Prerequisites

- **Rust** (stable, 1.77+): `rustup update stable`
- **Node.js** (20+) & **pnpm** (or npm/yarn)
- **CMake** + **clang/LLVM** (needed to compile whisper.cpp C++ code)
  - macOS: `brew install cmake llvm` (Xcode command line tools include clang)
  - Ubuntu: `sudo apt install cmake clang libclang-dev libasound2-dev`
  - Windows: Install Visual Studio C++ build tools + CMake + LLVM
- **macOS M-series**: Add to `src-tauri/.cargo/config.toml`:
  ```toml
  [target.aarch64-apple-darwin]
  rustflags = ["-lc++", "-l", "framework=Accelerate"]
  ```

## Step 1 — Bootstrap the Tauri v2 Project

```bash
# Create the project (React + TypeScript template)
pnpm create tauri-app@latest whisper-transcriber -- --template react-ts

cd whisper-transcriber
pnpm install
```

## Step 2 — Add Frontend Dependencies

```bash
pnpm add @tauri-apps/api@^2 @monaco-editor/react monaco-editor
```

## Step 3 — Add Rust Dependencies

```bash
cd src-tauri

cargo add tauri --features default
cargo add tauri-build --build
cargo add serde --features derive
cargo add serde_json
cargo add cpal@0.16
cargo add whisper-rs@0.15
cargo add tokio --features "rt-multi-thread sync macros"
cargo add ringbuf@0.4
cargo add rubato@0.16
cargo add hound@3.5

cd ..
```

## Step 4 — Download a Whisper Model

Download a GGML model into `src-tauri/models/`. The `base.en` model is a good balance of speed and quality (~150 MB):

```bash
mkdir -p src-tauri/models
curl -L -o src-tauri/models/ggml-base.en.bin \
  https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-base.en.bin
```

For faster but lower quality, use `ggml-tiny.en.bin`. For better quality, use `ggml-small.en.bin`.

## Step 5 — Replace Source Files

Replace the generated source files with the ones provided below.

## Step 6 — Update Tauri Config Permissions

Make sure `src-tauri/capabilities/default.json` includes event permissions:

```json
{
  "$schema": "../gen/schemas/desktop-schema.json",
  "identifier": "default",
  "description": "default permissions",
  "windows": ["main"],
  "permissions": [
    "core:default",
    "core:event:default",
    "core:event:allow-emit",
    "core:event:allow-listen"
  ]
}
```

## Step 7 — Run

```bash
pnpm tauri dev
```

---

## Architecture

```
whisper-transcriber/
├── src/                          # React frontend
│   ├── App.tsx                   # Main app component
│   ├── App.css                   # Styles
│   ├── Waveform.tsx              # Canvas waveform visualizer
│   ├── main.tsx                  # React entry point
│   └── vite-env.d.ts
├── index.html
├── src-tauri/
│   ├── src/
│   │   ├── lib.rs                # Tauri setup + commands
│   │   ├── main.rs               # Entry point
│   │   ├── audio.rs              # Microphone capture via cpal
│   │   └── transcribe.rs         # Whisper inference
│   ├── models/
│   │   └── ggml-base.en.bin      # Whisper model (you download)
│   ├── Cargo.toml
│   ├── tauri.conf.json
│   ├── capabilities/
│   │   └── default.json
│   └── .cargo/
│       └── config.toml           # (macOS M-series linker flags)
└── package.json
```

**Data flow:**
1. `audio.rs` captures mic via `cpal`, resamples to 16kHz mono f32
2. Every ~2 seconds of audio, a chunk is sent to `transcribe.rs`
3. `transcribe.rs` runs whisper inference and returns segment text
4. `lib.rs` emits `transcription-result` and `audio-waveform` events to the frontend
5. Frontend updates Monaco editor and canvas waveform
