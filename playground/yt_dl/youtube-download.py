from pytube import YouTube
from pathlib import Path
from typing import Union

def download_youtube_video(video_url: str, save_path:str) -> None:
    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Ensure the save path is a Path object
        save_path = Path(save_path)
        
        # Create the directory if it doesn't exist
        save_path.mkdir(parents=True, exist_ok=True)
        
        # Download the video to the specified path
        print(f"Downloading video: {yt.title}")
        stream.download(output_path=save_path)
        print(f"Download completed! Video saved to: {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = "https://youtu.be/a165Ex30H2Q"  # Replace with your video URL
    save_path = "data"  # Replace with your desired save path
    download_youtube_video(video_url, save_path)