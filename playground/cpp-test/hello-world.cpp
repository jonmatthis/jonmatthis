#include <iostream>
#include <iostream>
#include <opencv2/opencv.hpp>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
int main(int argc, char** argv) {
    // Use VideoCapture to capture video from camera index 0 (first camera)
    cv::VideoCapture cap(0);

    // Check if camera opened successfully
    if(!cap.isOpened()) {
        std::cerr << "Error: Could not open camera" << std::endl;
        return -1;
    }

    // Create a window to display the video
    cv::namedWindow("Webcam", cv::WINDOW_AUTOSIZE);

    cv::Mat frame;
    while(true) {
        // Capture a new frame from the camera
        cap >> frame;

        // Check if frame is empty, break if so
        if(frame.empty()) break;

        // Display the frame in the created window
        cv::imshow("Webcam", frame);

        // Break the loop if 'ESC' is pressed
        char c = (char) cv::waitKey(25);
        if(c==27) break;
    }

    // Release the VideoCapture object
    cap.release();

    // Close all OpenCV windows
    cv::destroyAllWindows();

    return 0;
}