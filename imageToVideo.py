# Project at: https://pypi.org/project/moviepy/
from moviepy.editor import *

# Sample image code taken from: https://www.tutorialexample.com/python-moviepy-convert-images-png-jpg-to-video-python-moviepy-tutorial/
# Sample audio code taken from: https://stackoverflow.com/a/55920417

# Images credit: https://www.pexels.com/@maumascaro
# files = ['img/712786.jpg', 'img/9192283.jpg']
# clip = ImageSequenceClip(files, fps = 4, durations=[100,1000])
clip = ImageClip("img/712786.jpg", duration=100)

# Sound credits: https://soundbible.com/royalty-free-sounds-1.html
audioclip = AudioFileClip("audio/bells-tibetan-daniel_simon.mp3")
new_audioclip = CompositeAudioClip([audioclip])
clip.audio = new_audioclip

clip.write_videofile("video.mp4", fps = 24)
