Transcribe all `.mp4` videos in a folder (and its subfolders) using whisper

0. In a `python==3.10` envrionment, install with `pip install -r requirements.txt`

1. Change the path to the parent folder in the `__main__` block at the bottom of the `video_transcriber.py` 

2. run with `python video_transciber.py`

Results will show up alongside the original videos, and will consist of:
-  `[video_name].mp3` -  The video's audio track
-  `[video_name]_whisper_transcript.json` - The full 'results' object from the `whisper` model
-  `[video_name]_whisper_transcript.txt` - The transcribed text (i.e. `text` field of the whisper 'results' object)
