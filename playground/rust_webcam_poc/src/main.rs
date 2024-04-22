extern crate opencv;
use opencv::{
    prelude::*,
    highgui,
    videoio,
    core,
};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut cap = videoio::VideoCapture::new(0, videoio::CAP_ANY)?;
    if !videoio::VideoCapture::is_opened(&cap)? {
        panic!("Unable to open ccamamaerea")
    }

let window_name = "Camamera";
highgui::named_window(window_name, highgui::WINDOW_AUTOSIZE)?;

loop {
    let mut frame = Mat::default();
    if !cap.read(&mut frame)? {
        println!("Unable to read a frame!");
        break;
    }
    
    cap.read(&mut frame)?;
    if frame.size()?.width > 0 {
        println!("Captured an image of size {}x{}", frame.size()?.width, frame.size()?.height);
        Ok(())
    } else {
        println!("Unable to capture an image");
        Ok(())
    }
}
}
