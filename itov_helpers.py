from moviepy.editor import *

# If filepath is "c:/path/to/filename.txt", then the return value of this
# function will be "filename" (without the file extension)
def getBaseFileName(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

def getListOfAudioFiles():
    audio_folder = "audio"
    audio_files = [audio_folder+'/'+audioFile for audioFile in os.listdir(audio_folder) if audioFile.endswith(".mp3")]
    return audio_files

def getListOfImageFiles():
    image_folder = "img"
    image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if (img.endswith(".png") or img.endswith(".jpg"))]
    return image_files


# Get and print list of files
# This is mainly used for testing
def printFiles():
    print("Get a list of files...")

    image_folder = "img"
    image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if (img.endswith(".png") or img.endswith(".jpg"))]
    imgFileCount = len(image_files)
    print("Image File Count: "),
    print(imgFileCount)
    print("List of image files")
    print(image_files)

    audio_folder = "audio"
    audio_files = [audio_folder+'/'+audioFile for audioFile in os.listdir(audio_folder) if audioFile.endswith(".mp3")]
    audioFileCount = len(audio_files)
    print("Audio File Count: "),
    print(audioFileCount)
    print("List of audio files")
    print(audio_files)
    print("Printing base audio filenames: ")
    for audioFile in audio_files:
        print(os.path.splitext(os.path.basename(audioFile))[0])
