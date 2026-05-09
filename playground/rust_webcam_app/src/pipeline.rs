//! Image processing pipeline: rotation and fast resize-to-fit.
//!
//! These operate on `image::RgbImage` which wraps a `Vec<u8>` — a contiguous
//! heap-allocated buffer of bytes, exactly like a NumPy `uint8` array backed
//! by a single allocation.
//!
//! ## Python / OpenCV / NumPy analogy
//!
//! `RgbImage` is `(height, width, 3)` bytes in row-major order with no padding,
//! i.e. `np.ndarray` of shape `(H, W, 3)` and dtype `np.uint8`.  The `image`
//! crate provides `rotate90`/`rotate180`/`rotate270` — the equivalent of
//! `cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)` etc.
//!
//! The custom nearest-neighbor resize works directly on raw `[u8]` slices,
//! which is conceptually identical to NumPy fancy-indexing with integer arrays:
//! ```python
//! src_y = (np.arange(dst_h) * src_h // dst_h).astype(int)
//! src_x = (np.arange(dst_w) * src_w // dst_w).astype(int)
//! dst = src[src_y[:, None], src_x]  # nearest-neighbor via broadcasting
//! ```
//! But in Rust we write the loops explicitly — the compiler auto-vectorizes them.

use image::RgbImage;

use crate::recorder::VideoRecorder;

// ── rotation ──────────────────────────────────────────────────────────

/// Apply a rotation to an image.
///
/// `rotation` encoding: 0 = 0°, 1 = 90° clockwise, 2 = 180°, 3 = 270° CW.
///
/// For 0° the image is returned unchanged (no copy).  The `image` crate
/// rotates in-place where possible for 180°, and allocates a new buffer for
/// 90° and 270° (because width and height swap).
///
/// Python analogy: `cv2.rotate()` with `ROTATE_90_CLOCKWISE` etc., though
/// OpenCV always returns a new array.
pub(crate) fn apply_rotation(image: RgbImage, rotation: u8) -> RgbImage {
    match rotation {
        0 => image,
        1 => image::imageops::rotate90(&image),
        2 => image::imageops::rotate180(&image),
        3 => image::imageops::rotate270(&image),
        _ => unreachable!(),
    }
}

/// Change the current rotation by `delta` steps (-1 = counterclockwise,
/// +1 = clockwise), wrapping with `rem_euclid` so it stays in 0..4.
///
/// Stops any active recording if the aspect ratio changes (0↔1 or 2↔3),
/// because video encoders typically can't handle mid-stream resolution changes.
///
/// ## Rust detail: `rem_euclid` vs `%`
///
/// Rust's `%` is the **remainder** operator (truncating toward zero), not
/// modulo.  For negative numbers this gives a different result than Python's
/// `%`.  `rem_euclid` matches Python's `%` behaviour (always non-negative).
/// Example: `-1 % 4` in Python is `3`; in Rust `-1 % 4` is `-1`, but
/// `(-1i8).rem_euclid(4)` is `3`.
pub(crate) fn change_rotation(
    current: u8,
    delta: i8,
    recorder: &mut Option<VideoRecorder>,
) -> u8 {
    let new = (current as i8 + delta).rem_euclid(4) as u8;

    if current % 2 != new % 2 {
        if let Some(active_recorder) = recorder.take() {
            println!("\nRotation changes aspect ratio — stopping recording.");
            let _ = active_recorder.finish();
        }
    }

    new
}

// ── fast resize ───────────────────────────────────────────────────────
//
// Works directly on raw `[u8]` slices, avoiding the per-pixel trait dispatch
// overhead of `image::imageops::resize`.  Integer ratio arithmetic (no float
// per pixel) keeps it fast even at 1080p.

/// Fast nearest-neighbor downscale to fit within `maximum_dimension`.
///
/// Operates on the raw `[u8]` byte slice to avoid per-pixel overhead.
///
/// ## How it works
///
/// For each destination pixel `(x, y)`, compute the source pixel by integer
/// ratio: `src_x = x * src_width / dst_width`.  This is nearest-neighbor
/// interpolation — the same algorithm as OpenCV's `INTER_NEAREST`.
///
/// Unlike `image::imageops::resize`, this function:
/// - Does no trait-dispatch per pixel (the `image` crate uses generic pixel
///   types, and the compiler can't always inline through the trait layer).
/// - Uses integer arithmetic exclusively (no `f32`→`usize` conversions per
///   pixel), which helps the compiler auto-vectorize.
/// - Maintains aspect ratio exactly via integer ratios.
///
/// ## Rust concept: allocations
///
/// `vec![0u8; N]` allocates a zero-filled `Vec<u8>` on the heap — similar to
/// `np.zeros(N, dtype=np.uint8)` but as a flat 1-D buffer.  Rust vectors
/// store their capacity and length separately (like a Python list), so they
/// can grow.  Here we preallocate the exact size needed.
///
/// `RgbImage::from_raw()` is a zero-cost conversion: it takes ownership of the
/// `Vec<u8>` and wraps it with width/height metadata.  No copy occurs.
pub(crate) fn fast_resize_to_fit(image: RgbImage, maximum_dimension: u32) -> RgbImage {
    let (width, height) = (image.width(), image.height());
    let maximum_side = width.max(height);
    if maximum_side <= maximum_dimension {
        return image;
    }

    let (mut new_width, mut new_height) = if width > height {
        (
            maximum_dimension,
            (height as u64 * maximum_dimension as u64 / width as u64) as u32,
        )
    } else {
        (
            (width as u64 * maximum_dimension as u64 / height as u64) as u32,
            maximum_dimension,
        )
    };
    // H.264 yuv420p (and many other codecs) require even dimensions because
    // chroma subsampling operates on 2×2 pixel blocks.  Mask off the low bit.
    new_width &= !1;
    new_height &= !1;

    let source = image.as_raw();
    let source_width = width as usize;
    let source_height = height as usize;
    let destination_width = new_width as usize;
    let destination_height = new_height as usize;
    let mut destination = vec![0u8; destination_width * destination_height * 3];

    for y in 0..destination_height {
        let source_y = y * source_height / destination_height;
        let source_row = source_y * source_width * 3;
        let destination_row = y * destination_width * 3;

        for x in 0..destination_width {
            let source_x = x * source_width / destination_width;
            let source_index = source_row + source_x * 3;
            let destination_index = destination_row + x * 3;
            // Copy all three RGB channels from the source pixel
            destination[destination_index] = source[source_index];
            destination[destination_index + 1] = source[source_index + 1];
            destination[destination_index + 2] = source[source_index + 2];
        }
    }

    RgbImage::from_raw(new_width, new_height, destination)
        .expect("resize dimensions must be non-zero")
}
