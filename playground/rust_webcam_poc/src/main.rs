extern crate opencv;
use opencv::{
    prelude::*,
    videoio,
};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut cap = videoio::VideoCapture::new(0, videoio::CAP_ANY)?;
    if !videoio::VideoCapture::is_opened(&cap)? {
        panic!("Unable to open ccamamaerea")
    }
    let mut frame = Mat::default();
    cap.read(&mut frame)?;
    if frame.size()?.width > 0 {
        println!("Captured an image of size {}x{}", frame.size()?.width, frame.size()?.height);
    } else {
        println!("Unable to capture an image");
    }
}
