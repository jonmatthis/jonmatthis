extern crate opencv;
use opencv::{highgui, prelude::*, videoio};
use std::sync::mpsc;
use std::thread;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut cap = videoio::VideoCapture::new(0, videoio::CAP_ANY)?;
    if !videoio::VideoCapture::is_opened(&cap)? {
        panic!("Unable to open camera");
    }

    // Set the frame width and height to 1280x720
    videoio::VideoCapture::set(&mut cap, videoio::CAP_PROP_FRAME_WIDTH, 1280.0)?;
    videoio::VideoCapture::set(&mut cap, videoio::CAP_PROP_FRAME_HEIGHT, 720.0)?;

    let window_name = "Camera";
    highgui::named_window(window_name, highgui::WINDOW_AUTOSIZE)?;

    let (tx, rx) = mpsc::channel();
    
    // Move 'cap' into the spawned thread
    let cap_thread = thread::spawn(move || {
    loop {
        let mut frame = Mat::default();
            if !cap.read(&mut frame).expect("Failed to read frame") {
                println!("Unable to read a frame in thread!");
            break;
        }
            tx.send(frame).expect("Failed to send frame");
        }
    });

    for frame in rx {
        if frame.size()?.width > 0 {
            highgui::imshow(window_name, &frame)?;
            if highgui::wait_key(1)? > 0 {
                break;
            }
        } else {
            println!("No image captured, frame is empty.");
        }
    }

    // Ensure the capture thread closes gracefully by joining it
    cap_thread.join().expect("The capture thread has panicked");

    Ok(())
}
