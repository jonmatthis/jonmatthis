from pytube import YouTube

def download_youtube_video(video_url):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f"Downloading video: {yt.title}")
        stream.download()
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = "https://youtu.be/a165Ex30H2Q"  # Replace with your video URL
    download_youtube_video(video_url)