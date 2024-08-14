from pathlib import Path
from moviepy.editor import VideoFileClip
from typing import List

def extract_audio_from_videos(directory: str) -> None:
    """
    Recursively searches for .mp4 and .MP4 files in the specified directory,
    extracts their audio, and saves it as .mp3 files with '_audio' appended to the original name.

    Parameters
    ----------
    directory : str
        The directory to search for video files.

    Examples
    --------
    >>> extract_audio_from_videos('/path/to/directory')
    """
    path = Path(directory)
    video_extensions = ['.mp4', '.MP4']
    
    for video_file in path.rglob('*'):
        if video_file.suffix in video_extensions:
            with VideoFileClip(str(video_file)) as video:
                audio = video.audio
                audio_output_path = video_file.with_name(f"{video_file.stem}_audio.mp3")
                audio.write_audiofile(audio_output_path)

if __name__ == "__main__":
    directory = "/path/to/your/folder"
    extract_audio_from_videos(directory)
