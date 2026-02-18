use std::path::Path;

use whisper_rs::{FullParams, SamplingStrategy, WhisperContext, WhisperContextParameters, WhisperState};

/// Holds a loaded whisper model context, ready to create inference states.
pub struct Transcriber {
    ctx: WhisperContext,
}

/// A single transcription segment with start/end timestamps in milliseconds.
#[derive(Clone, Debug, serde::Serialize)]
pub struct Segment {
    pub start_ms: i64,
    pub end_ms: i64,
    pub text: String,
}

impl Transcriber {
    /// Load a GGML whisper model from the given path.
    pub fn new(model_path: &Path) -> Transcriber {
        assert!(
            model_path.exists(),
            "Whisper model not found at: {}",
            model_path.display()
        );
        let ctx = WhisperContext::new_with_params(
            model_path.to_str().expect("Invalid model path encoding"),
            WhisperContextParameters::default(),
        )
        .expect("Failed to load whisper model");

        Transcriber { ctx }
    }

    /// Create a new inference state. Each concurrent transcription needs its own state.
    pub fn create_state(&self) -> WhisperState {
        self.ctx
            .create_state()
            .expect("Failed to create whisper state")
    }

    /// Run inference on a chunk of 16kHz mono f32 audio.
    /// Returns transcribed segments.
    pub fn transcribe(state: &mut WhisperState, audio_16khz: &[f32]) -> Vec<Segment> {
        let mut params = FullParams::new(SamplingStrategy::Greedy { best_of: 1 });

        // Optimize for real-time: single-threaded, no timestamps token, translate=false
        params.set_n_threads(4);
        params.set_language(Some("en"));
        params.set_translate(false);
        params.set_no_context(true);
        params.set_single_segment(true);
        params.set_print_special(false);
        params.set_print_progress(false);
        params.set_print_realtime(false);
        params.set_print_timestamps(false);
        // Suppress non-speech tokens
        params.set_suppress_blank(true);
        params.set_suppress_non_speech_tokens(true);

        state
            .full(params, audio_16khz)
            .expect("Whisper inference failed");

        let num_segments = state.full_n_segments().expect("Failed to get segment count");
        let mut segments = Vec::with_capacity(num_segments as usize);

        for i in 0..num_segments {
            let text = state
                .full_get_segment_text(i)
                .expect("Failed to get segment text");
            let start = state
                .full_get_segment_t0(i)
                .expect("Failed to get segment start timestamp");
            let end = state
                .full_get_segment_t1(i)
                .expect("Failed to get segment end timestamp");

            let trimmed = text.trim().to_string();
            if !trimmed.is_empty() {
                segments.push(Segment {
                    start_ms: start as i64 * 10, // whisper timestamps are in centiseconds
                    end_ms: end as i64 * 10,
                    text: trimmed,
                });
            }
        }

        segments
    }
}
