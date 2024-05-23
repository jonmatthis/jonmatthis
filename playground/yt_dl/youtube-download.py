import yt_dlp
from pathlib import Path

def download_youtube_video(video_url: str, save_path: str) -> None:
    save_path = Path(save_path)
    save_path.mkdir(parents=True, exist_ok=True)
    
    ydl_opts = {
        'format': 'best',  # download the best available quality
        'outtmpl': str(save_path / '%(title)s.%(ext)s'),  # output path and file format
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    video_url = "https://youtu.be/a165Ex30H2Q"  # Replace with your video URL
    save_path = "data"  # Replace with your desired save path
    download_youtube_video(video_url, save_path)