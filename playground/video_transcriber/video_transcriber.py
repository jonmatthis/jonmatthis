from pathlib import Path
from audio_extract import extract_audio
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_audio_from_videos(directory: str, exclude: List[str] = None) -> None:
    """
    Recursively searches for .mp4 files (case-insensitive) in the specified directory,
    extracts their audio, and saves it as .mp3 files with '_audio' appended to the original name.

    Parameters
    ----------
    directory : str
        The directory to search for video files.
    exclude : List[str], optional
        List of file or folder names to exclude from processing.

    Examples
    --------
    >>> extract_audio_from_videos('/path/to/directory', exclude=['exclude_folder', 'exclude_file.mp4'])
    """
    if exclude is None:
        exclude = []

    path = Path(directory)

    logging.info(f"Starting audio extraction in directory: {directory}")
    for video_file in path.rglob('*'):
        if any(ex in video_file.parts for ex in exclude) or video_file.name in exclude:
            logging.info(f"Skipping excluded file or folder: {video_file}")
            continue
        if video_file.suffix.lower() == '.mp4':
            audio_output_path = video_file.with_name(f"{video_file.stem}_audio.mp3")
            try:
                extract_audio(input_path=str(video_file), output_path=str(audio_output_path))
                logging.info(f"Extracted audio from {video_file} to {audio_output_path}")
            except Exception as e:
                logging.error(f"Failed to extract audio from {video_file}: {e}")

    logging.info("Audio extraction completed.")

if __name__ == "__main__":
    directory = r"D:\videos\obs-recordings\2024-08-09"
    exclude = ['exclude_folder', 'exclude_file.mp4']
    extract_audio_from_videos(directory, exclude)