# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose & User Context

This is a **learning project** for the user to gain Rust proficiency. It is deliberately small: a webcam preview/recording app that exercises real-world systems-programming concerns (threads, channels, FFI-adjacent boundaries, raw pixel buffers).

**User background:**
- Deep expertise in Python — NumPy, OpenCV, and camera pipelines in particular.
- Author of the **FreeMoCap** project and **SkellyCam**, which do high-performance multi-camera synchronized recording and streaming in Python.
- Growing experience with TypeScript/JavaScript and Electron frontends.
- **Almost no Rust experience** — this project is the jumping-off point.

**Motivation:** The long-term goal is to evaluate and adopt Rust for performance-critical, multi-camera, synchronized recording and streaming workloads that are currently implemented in Python/OpenCV. This webcam app is a deliberate first step: it touches threads, channels, raw memory, and timing — all the primitives a multi-camera system would need.

**How to interact with the user:**
- When explaining Rust concepts, draw explicit analogies to Python, NumPy, and OpenCV. For example: "Rust's `mpsc::channel` is like Python's `queue.Queue` but with compile-time type guarantees and no GIL contention," or "Rust's `Vec<u8>` is a contiguous heap-allocated buffer — think of it like a NumPy `uint8` array backed by a single allocation."
- Highlight differences that matter for performance: stack vs. heap, ownership vs. reference counting, monomorphization vs. dynamic dispatch, compile-time vs. runtime checks.
- Call out Rust idioms that have no direct Python equivalent (lifetimes, borrow checker, `Send`/`Sync`, pattern matching on enums).
- This is a teaching environment — prioritize clarity and explanation over terseness.

## Build & Run

```bash
cargo build              # Debug build
cargo build --release    # Release build
cargo run                # Run with defaults (camera 0)
cargo run -- --list      # List available cameras
cargo run -- -c 1 -o out.mp4  # Camera 1, custom output path
cargo check              # Quick compile check (no binary)
```

There are no tests yet in this project.

**Recording requires `ffmpeg`** on the system PATH. Recording pipes raw RGB24 frames to an ffmpeg subprocess encoding to H.264 MP4.

## Architecture

The app has four modules, all in `src/` (flat layout):

### `main.rs` — CLI, main loop, frame pipeline, helpers

- Uses `clap` derive for CLI args: camera index, list flag, output path, resolution, FPS, max display dimension.
- **Main loop** runs on the main thread, processing one frame per iteration through these stages, each individually timed:
  1. Keyboard input (minifb key polling)
  2. Receive `CameraEvent::Frame` from camera thread via `mpsc::sync_channel`
  3. Rotation (0°/90°/180°/270° via `image::imageops`)
  4. Scale-to-fit if `--maximum-dimension` is set (custom integer-ratio nearest-neighbor resize on raw `[u8]`)
  5. Recreate display window if dimensions changed
  6. Feed raw RGB bytes to recorder (if active)
  7. RGB→ARGB conversion + `minifb` buffer update
- Keyboard shortcuts: Q/Esc quit, R toggle recording, S print settings, 1-9 select control, ↑↓ adjust, ←→ rotate.
- Per-stage timing printed every 60 frames (microsecond averages).

### `camera.rs` — Camera thread & channel protocol

- **Thread-per-camera model**: `spawn_camera_thread()` opens the camera on a dedicated thread so platform-specific init (COM STA on Windows, AVFoundation session on macOS, V4L2 on Linux) stays on that thread. The camera object itself is `!Send` by design — only decoded `RgbImage` (owned `Vec<u8>`) and primitives cross thread boundaries via channels.
- Channel types:
  - `CameraCommand` (enum sent to thread): `AdjustControl`, `GetControlInfo`, `Shutdown`
  - `CameraEvent` (enum sent from thread): `Frame(FramePacket)`, `ControlAdjusted`, `ControlInfo`, `Error`
- `CameraManager` (crate-internal) owns the `nokhwa::Camera` and wraps capture, control query, and control adjustment with type-aware step/clamp logic for integer ranges, float ranges, etc.
- `CameraMetadata` is gathered on the main thread via a temporary open-query-close cycle (`query_camera()`) before spawning the persistent camera thread, so main knows resolution and supported controls upfront.

### `display.rs` — Window & overlay rendering

- Wraps `minifb::Window` with resize support (`Scale::FitScreen`).
- RGB→ARGB conversion uses unsafe raw pointer indexing (not iterator `zip`) so the compiler can auto-vectorize.
- `update_dimensions()` tears down and recreates the window when frame size changes (e.g., after rotation swaps width/height).
- Built-in 5×7 bitmap font (ASCII 32–90) for on-screen overlay bars. `draw_overlay()` renders a proportional-height status bar at the bottom of the frame with recording status, FPS, rotation, and selected control info.

### `recorder.rs` — ffmpeg subprocess recorder

- Spawns `ffmpeg` with `-f rawvideo -pixel_format rgb24` reading from `pipe:0`.
- Encodes to H.264 (libx264) with `ultrafast` preset and `yuv420p` pixel format.
- `feed_frame()` writes raw `&[u8]` to ffmpeg's stdin. `finish()` drops stdin (sends EOF) and waits for ffmpeg to exit.
- `Drop` impl kills ffmpeg if `finish()` is never called (safety net for early exit).

## Dependencies

| Crate | Purpose |
|-------|---------|
| `nokhwa` (input-native) | Cross-platform camera capture |
| `image` | Image rotation (90°/180°/270°) and `RgbImage` type |
| `minifb` | Cross-platform window and keyboard input |
| `clap` (derive) | CLI argument parsing |
| `anyhow` | Error propagation |
