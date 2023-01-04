import moviepy.editor
from pathlib import Path

video_file = Path('the_name_of_the_video_file') #for example 'my_video_file.mp4' 

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.mp3')