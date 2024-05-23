from pytube import YouTube
import os

def download_youtube_video(video_url:str, save_path:str):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Ensure the save path directory exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        # Download the video to the specified path
        print(f"Downloading video: {yt.title}")
        stream.download(output_path=save_path)
        print(f"Download completed! Video saved to: {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = "YOUR_YOUTUBE_VIDEO_URL_HERE"  # Replace with your video URL
    save_path = "data/"  # Replace with your desired save path
    download_youtube_video(video_url, save_path)