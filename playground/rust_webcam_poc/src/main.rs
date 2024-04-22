extern crate opencv;
use opencv::{
    highgui,
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
}