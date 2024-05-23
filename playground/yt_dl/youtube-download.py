from pytube import YouTube
from pathlib import Path
from typing import Union

def download_youtube_video(video_url: str, save_path: str) -> None:
    print(f"Downloading {video_url} to {save_path}")
    try:
        # Create a YouTube object
        yt = YouTube(video_url, on_progress_callback=progress_function, on_complete_callback=complete_function)
        print(f"Found video: {yt.title}")

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        print(f"Found stream: {stream.resolution}")
        
        # Ensure the save path is a Path object
        save_path = Path(save_path)
        
        # Create the directory if it doesn't exist
        save_path.mkdir(parents=True, exist_ok=True)
        
        # Download the video to the specified path
        print(f"Downloading video: {yt.title}")
        stream.download(output_path=save_path)
        print(f"Download completed! Video saved to: {save_path}")
    except KeyError as e:
        print(f"KeyError: {e}")
    except AttributeError as e:
        print(f"AttributeError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def progress_function(stream, chunk, bytes_remaining):
    print(f"Downloaded {stream.filesize - bytes_remaining} of {stream.filesize} bytes...")

def complete_function(stream, file_path):
    print(f"Download complete: {file_path}")

if __name__ == "__main__":
    video_url = "https://youtu.be/a165Ex30H2Q"  # Replace with your video URL
    save_path = "data"  # Replace with your desired save path
    download_youtube_video(video_url, save_path)