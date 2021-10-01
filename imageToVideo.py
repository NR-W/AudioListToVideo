# Project at: https://pypi.org/project/moviepy/
from moviepy.editor import *

import itov_helpers

# Sample image code taken from: https://www.tutorialexample.com/python-moviepy-convert-images-png-jpg-to-video-python-moviepy-tutorial/
# Sample audio code taken from: https://stackoverflow.com/a/55920417

# Sound credits: https://soundbible.com/royalty-free-sounds-1.html
audioFilePath = "audio/bells-tibetan-daniel_simon.mp3"
audioclip = AudioFileClip(audioFilePath)
new_audioclip = CompositeAudioClip([audioclip])

# Give the video 2 more seconds of runtime so that the end is not too abrupt
audioduration = 0
audioduration = audioclip.duration
videoduration = audioduration + 2

# Images credit: https://www.pexels.com/@maumascaro
# files = ['img/712786.jpg', 'img/9192283.jpg', 'img/9192253.jpg']
# clip = ImageSequenceClip(files, fps = 4, durations=[100,1000])
# clip = ImageClip("img/712786.jpg", duration=100)
imageFilePath = "img/9192253.jpg"
clip = ImageClip(imageFilePath, duration=videoduration)

# videoBaseName = os.path.splitext(os.path.basename(audioFilePath))[0]
videoBaseName = itov_helpers.getBaseFileName(audioFilePath)
clip.audio = new_audioclip
# clip.write_videofile("video.mp4", fps = 24)
clip.write_videofile(videoBaseName + ".mp4", fps = 24)

# # Get and print list of files
# itov_helpers.printFiles()
