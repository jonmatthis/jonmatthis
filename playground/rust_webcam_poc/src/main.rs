extern crate opencv;
use opencv::{
    prelude::*,
    videoio,
    highgui,
    core,
};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut cap = videoio::VideoCapture::new(0, videoio::CAP_ANY)?;
    if !videoio::VideoCapture::is_opened(&cap)? {
        panic!("Unable to open camera");
    }

    // Set the frame width and height to 1920x1080
    videoio::VideoCapture::set(&mut cap, videoio::CAP_PROP_FRAME_WIDTH, 1920.0)?;
    videoio::VideoCapture::set(&mut cap, videoio::CAP_PROP_FRAME_HEIGHT, 1080.0)?;

    // Optionally, set the frame rate (depending on camera and driver support)
    // videoio::VideoCapture::set(&mut cap, videoio::CAP_PROP_FPS, 30.0)?;
    let window_name = "Camera";
    highgui::named_window(window_name, highgui::WINDOW_AUTOSIZE)?;

loop {
    let mut frame = Mat::default();
    if !cap.read(&mut frame)? {
        println!("Unable to read a frame!");
        break;
    }

    if frame.size()?.width > 0 {
        println!("Captured an image of size {}x{}", frame.size()?.width, frame.size()?.height);
            highgui::imshow(window_name, &frame)?;
        if highgui::wait_key(10)? > 0 {
            break;
            }
    } else {
            println!("No image captured, frame is empty.");
    }
}

Ok(())
}
