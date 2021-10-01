"""
This is the main file for executing the Tool functionality.
When this file is run, a video file will be generated for each audio file found  in
the audio/ directory.
This tool is dependent on the MoviePy project (https://pypi.org/project/moviepy).
"""

from moviepy.editor import *
import itov_helpers

outputPath = "out/"

# Load the lists of Audio and Image files available.
audio_files = itov_helpers.getListOfAudioFiles()
image_files = itov_helpers.getListOfImageFiles()
imgFileCount = len(image_files)
img_counter = 0

# Create a video file for each audio file available.
for audioFilePath in audio_files:
    # Load the audio file as a Video Audio Clip.
    audioclip = AudioFileClip(audioFilePath)
    new_audioclip = CompositeAudioClip([audioclip])

    # Give the video 2 more seconds of runtime so that the end is not too abrupt
    audioduration = 0
    audioduration = audioclip.duration
    videoduration = audioduration + 2

    # When indexing the list of Image Files, we use Modulo with the number of
    # image files because, if there are more audio files than images, then this
    # will allow us to loop back to the first image (instead of running out of images to use).
    imageFilePath = image_files[img_counter%imgFileCount]
    img_counter += 1
    clip = ImageClip(imageFilePath, duration=videoduration)

    # Generate the filename and create the video file for each corresponding audio.
    videoBaseName = itov_helpers.getBaseFileName(audioFilePath)
    clip.audio = new_audioclip
    clip.write_videofile(outputPath + videoBaseName + ".mp4", fps = 24)
