mod audio;
mod transcribe;

use std::path::PathBuf;
use std::sync::atomic::Ordering;
use std::sync::Mutex;
use std::time::Duration;

use tauri::{AppHandle, Emitter, Manager};

use crate::audio::{resample_linear, AudioCapture};
use crate::transcribe::Transcriber;

/// Waveform payload sent to the frontend for visualization.
#[derive(Clone, serde::Serialize)]
struct WaveformPayload {
    /// Downsampled amplitude values for drawing, normalized to [-1, 1]
    samples: Vec<f32>,
}

/// Transcription result payload sent to the frontend.
#[derive(Clone, serde::Serialize)]
struct TranscriptionPayload {
    text: String,
}

/// Mutable state shared between commands and the capture loop.
struct AppState {
    capture: Option<AudioCapture>,
}

/// Resolve the model path relative to the executable or src-tauri/models/ during development.
fn resolve_model_path() -> PathBuf {
    // In development, the binary is in src-tauri/target/debug/
    // Try walking up to find src-tauri/models/
    let exe = std::env::current_exe().expect("Failed to get executable path");
    let exe_dir = exe.parent().expect("Failed to get executable directory");

    // Production: model next to the binary
    let beside_exe = exe_dir.join("models").join("ggml-base.en.bin");
    if beside_exe.exists() {
        return beside_exe;
    }

    // Development: walk up from target/debug/ to src-tauri/models/
    let mut dir = exe_dir.to_path_buf();
    for _ in 0..5 {
        let candidate = dir.join("models").join("ggml-base.en.bin");
        if candidate.exists() {
            return candidate;
        }
        if !dir.pop() {
            break;
        }
    }

    // Fallback: current working directory
    let cwd = std::env::current_dir().expect("Failed to get CWD");
    let cwd_candidate = cwd.join("src-tauri").join("models").join("ggml-base.en.bin");
    assert!(
        cwd_candidate.exists(),
        "Could not find whisper model. Looked at:\n  {}\n  {}\nPlease download ggml-base.en.bin into src-tauri/models/",
        beside_exe.display(),
        cwd_candidate.display()
    );
    cwd_candidate
}

#[tauri::command]
fn start_listening(app: AppHandle, state: tauri::State<'_, Mutex<AppState>>) {
    let mut s = state.lock().expect("State lock poisoned");
    if s.capture.is_some() {
        // Already running
        return;
    }

    let capture = AudioCapture::start();
    let device_sample_rate = capture.sample_rate;
    s.capture = Some(capture);
    drop(s);

    // Load the whisper model in a background thread
    let model_path = resolve_model_path();
    let app_handle = app.clone();
    let state_handle = app.state::<Mutex<AppState>>().inner().clone();

    std::thread::Builder::new()
        .name("transcription-loop".into())
        .spawn(move || {
            let transcriber = Transcriber::new(&model_path);
            let mut whisper_state = transcriber.create_state();

            // Accumulate ~2 seconds of 16kHz audio before running inference
            let chunk_duration_secs = 2.0;
            let target_rate: u32 = 16000;
            let samples_per_chunk = (target_rate as f64 * chunk_duration_secs) as usize;
            let mut accumulated_16khz: Vec<f32> = Vec::with_capacity(samples_per_chunk * 2);

            loop {
                std::thread::sleep(Duration::from_millis(100));

                // Drain samples from the ring buffer
                let raw_samples = {
                    let mut s = state_handle.lock().expect("State lock poisoned");
                    match s.capture.as_mut() {
                        Some(cap) => {
                            if !cap.is_running.load(Ordering::Relaxed) {
                                break;
                            }
                            cap.drain_samples()
                        }
                        None => break,
                    }
                };

                if raw_samples.is_empty() {
                    continue;
                }

                // Send waveform data to frontend (downsample for visualization)
                let waveform_samples = downsample_for_viz(&raw_samples, 200);
                let _ = app_handle.emit(
                    "audio-waveform",
                    WaveformPayload {
                        samples: waveform_samples,
                    },
                );

                // Resample to 16kHz for whisper
                let resampled = resample_linear(&raw_samples, device_sample_rate, target_rate);
                accumulated_16khz.extend_from_slice(&resampled);

                // Once we have enough audio, run transcription
                if accumulated_16khz.len() >= samples_per_chunk {
                    let chunk: Vec<f32> = accumulated_16khz.drain(..).collect();

                    let segments = Transcriber::transcribe(&mut whisper_state, &chunk);

                    for seg in &segments {
                        let _ = app_handle.emit(
                            "transcription-result",
                            TranscriptionPayload {
                                text: seg.text.clone(),
                            },
                        );
                    }
                }
            }
        })
        .expect("Failed to spawn transcription thread");
}

#[tauri::command]
fn stop_listening(state: tauri::State<'_, Mutex<AppState>>) {
    let mut s = state.lock().expect("State lock poisoned");
    if let Some(ref capture) = s.capture {
        capture.is_running.store(false, Ordering::Relaxed);
    }
    s.capture = None;
}

/// Downsample a buffer to `target_len` points by taking max absolute value in each bucket.
/// This preserves peaks for waveform visualization.
fn downsample_for_viz(samples: &[f32], target_len: usize) -> Vec<f32> {
    if samples.len() <= target_len {
        return samples.to_vec();
    }
    let bucket_size = samples.len() / target_len;
    samples
        .chunks(bucket_size)
        .map(|chunk| {
            chunk
                .iter()
                .copied()
                .max_by(|a, b| a.abs().partial_cmp(&b.abs()).unwrap())
                .unwrap_or(0.0)
        })
        .collect()
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .manage(Mutex::new(AppState { capture: None }))
        .invoke_handler(tauri::generate_handler![start_listening, stop_listening])
        .run(tauri::generate_context!())
        .expect("Failed to run Tauri application");
}
