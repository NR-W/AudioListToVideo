# AudioListToVideo
AudioListToVideo is a tool for creating a (static image) video for each audio file in a list.

## Introduction
The purpose of this script is to iterate through a list of audio files and a list of image files, and create a video for each audio file by combining it with an image. This can be used to upload sound bits as short videos to Youtube.

If there are more audio files than images, then the script will loop back and reuse image files.

## Requirements
You may need to install package MoviePy (if you haven't already). You can do this by executing:

```bash
pip install moviepy
```

Other reference: https://pypi.org/project/moviepy/

Note: I have forked the MoviePy to have the library accessible, in case any change to the main library breaks any functionality.

## Usage
To generate video files using this script, copy your audio files into the audio/ directory and copy the images you wish to use into the img/ directory. Replace existing sample audio/image files before copying your own. File audioToVideo.py is the (main) file to execute when you are ready to generate your videos. This will generate the videos and save them in the out/ directory.

```bash
python audioToVideo.py
```

Note: this script has only been tested with Python 3 in Windows 10.

## Contributing
Though contributions are welcome, I am not actively maintaining this repository, so it might take a while for me to respond to anything related to this.

## License
[MIT](https://choosealicense.com/licenses/mit/)
