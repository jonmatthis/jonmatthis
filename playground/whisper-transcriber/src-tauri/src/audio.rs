use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;

use cpal::traits::{DeviceTrait, HostTrait, StreamTrait};
use cpal::{SampleFormat, Stream};
use ringbuf::traits::{Consumer, Producer, Split};
use ringbuf::HeapRb;

/// Holds the audio capture stream and a ring buffer consumer for reading samples.
/// Samples are f32 mono at the device's native sample rate.
pub struct AudioCapture {
    _stream: Stream,
    pub consumer: ringbuf::HeapCons<f32>,
    pub sample_rate: u32,
    pub is_running: Arc<AtomicBool>,
}

impl AudioCapture {
    /// Opens the default input device and starts capturing audio.
    /// Samples are pushed into a ring buffer (~10 seconds at native rate).
    pub fn start() -> AudioCapture {
        let host = cpal::default_host();
        let device = host
            .default_input_device()
            .expect("No input device available");

        let supported_config = device
            .default_input_config()
            .expect("No supported input config");

        let sample_rate = supported_config.sample_rate().0;
        let channels = supported_config.channels() as usize;

        // Ring buffer sized for ~10 seconds of mono audio
        let rb = HeapRb::<f32>::new(sample_rate as usize * 10);
        let (mut producer, consumer) = rb.split();

        let is_running = Arc::new(AtomicBool::new(true));
        let running_flag = is_running.clone();

        let err_fn = |err: cpal::StreamError| {
            panic!("Audio stream error: {err}");
        };

        let stream = match supported_config.sample_format() {
            SampleFormat::F32 => device
                .build_input_stream(
                    &supported_config.into(),
                    move |data: &[f32], _: &cpal::InputCallbackInfo| {
                        if !running_flag.load(Ordering::Relaxed) {
                            return;
                        }
                        // Mix down to mono by averaging channels
                        for frame in data.chunks(channels) {
                            let mono: f32 =
                                frame.iter().sum::<f32>() / channels as f32;
                            // Drop samples if ring buffer is full (back-pressure)
                            let _ = producer.try_push(mono);
                        }
                    },
                    err_fn,
                    None,
                )
                .expect("Failed to build f32 input stream"),
            SampleFormat::I16 => device
                .build_input_stream(
                    &supported_config.into(),
                    move |data: &[i16], _: &cpal::InputCallbackInfo| {
                        if !running_flag.load(Ordering::Relaxed) {
                            return;
                        }
                        for frame in data.chunks(channels) {
                            let mono: f32 = frame.iter().map(|&s| s as f32 / 32768.0).sum::<f32>()
                                / channels as f32;
                            let _ = producer.try_push(mono);
                        }
                    },
                    err_fn,
                    None,
                )
                .expect("Failed to build i16 input stream"),
            other => panic!("Unsupported sample format: {other:?}"),
        };

        stream.play().expect("Failed to start audio stream");

        AudioCapture {
            _stream: stream,
            consumer,
            sample_rate,
            is_running,
        }
    }

    /// Drain all available samples from the ring buffer into a Vec.
    pub fn drain_samples(&mut self) -> Vec<f32> {
        let available = self.consumer.occupied_len();
        let mut buf = vec![0.0f32; available];
        let read = self.consumer.pop_slice(&mut buf);
        buf.truncate(read);
        buf
    }
}

/// Resample audio from `from_rate` to `to_rate` using linear interpolation.
/// This is a simple resampler suitable for speech (not music production).
pub fn resample_linear(samples: &[f32], from_rate: u32, to_rate: u32) -> Vec<f32> {
    if from_rate == to_rate {
        return samples.to_vec();
    }
    let ratio = from_rate as f64 / to_rate as f64;
    let output_len = (samples.len() as f64 / ratio).ceil() as usize;
    let mut output = Vec::with_capacity(output_len);
    for i in 0..output_len {
        let src_idx = i as f64 * ratio;
        let idx_floor = src_idx.floor() as usize;
        let frac = (src_idx - idx_floor as f64) as f32;
        let a = samples.get(idx_floor).copied().unwrap_or(0.0);
        let b = samples.get(idx_floor + 1).copied().unwrap_or(a);
        output.push(a + frac * (b - a));
    }
    output
}
