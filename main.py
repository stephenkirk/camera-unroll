""" Requires https://mediaarea.net/en/MediaInfo/Download/Mac_OS """
import os
from PIL import Image
from PIL import ExifTags
import subprocess
import re
import numpy as np

# Constants
FOLDER_PATH = os.path.expanduser("/Users/stephen/OneDrive - Stephen Kirk AB/Photography/Phone/Phone")
FILE_NAMES = [f for f in os.listdir(FOLDER_PATH) if os.path.isfile(FOLDER_PATH + f)]

# Example images
ex_compressed_meme = "IMG_3940 1.JPG"
ex_glitche = "IMG_3932.JPG"
ex_screenshot = "IMG_3931.PNG"
ex_snapchat_screenshot = "IMG_3922.PNG"
ex_snapchat_video = "RHYH3563.MP4"
ex_snapchat_image = "IMG_3903.JPG"
ex_regular_video = "IMG_3217.MOV"
ex_vsco = "JWBO4754.JPG"

## Image class?

def get_file_types(file_name):
    """Returns the type of file."""
    extension = file_name.lower().split('.')[-1]
    image_extensions = ['jpg', 'png', 'gif']
    video_extensions = ['mp3', 'mp4', 'mov', 'aae']
    if extension in image_extensions:
        return "Image", extension
    elif extension in video_extensions:
        return "Video", extension
    else:
        return "Other", extension

class Img:
    def __init__(self, file_path):
        self.tags = get_file_types(file_path)
        self.file_path = file_path
        self.get_tags()
    
    def test(self):
        return 42
    
    def get_tags(self):
        return [42]

x = Img(ex_snapchat_video)
x