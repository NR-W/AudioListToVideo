

# Sample code from: https://pypi.org/project/moviepy/
# from moviepy.editor import *
# video = VideoFileClip("myHolidays.mp4").subclip(50,60)
#
# # Make the text. Many more options are available.
# txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
#              .set_position('center')
#              .set_duration(10) )
#
# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
# result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...


# Sample image code taken from: https://www.tutorialexample.com/python-moviepy-convert-images-png-jpg-to-video-python-moviepy-tutorial/
# Sample audio code taken from: https://stackoverflow.com/a/55920417
from moviepy.editor import *

# files = ['1.png', '2.png', '3.png', '4.png']
# Image credit: https://www.pexels.com/@maumascaro
files = ['img/712786.jpg', 'img/9192283.jpg']
# clip = ImageSequenceClip(files, fps = 4)
# clip = ImageSequenceClip(files, fps = 4, durations=[100,1000])
clip = ImageClip("img/712786.jpg", duration=100)

# Sound credits: https://soundbible.com/royalty-free-sounds-1.html
audioclip = AudioFileClip("audio/bells-tibetan-daniel_simon.mp3")
new_audioclip = CompositeAudioClip([audioclip])
clip.audio = new_audioclip

clip.write_videofile("video.mp4", fps = 24)


# # Sample code from: https://stackoverflow.com/a/62434934
# import os
# import moviepy.video.io.ImageSequenceClip
# image_folder='folder_with_images'
# fps=1
#
# # image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".jpg")]
# image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".png")]
# clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
# clip.write_videofile('my_video.mp4')
