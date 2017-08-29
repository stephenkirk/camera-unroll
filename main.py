"""aaah"""
import os
from PIL import Image
from PIL import ExifTags

def get_file_format(file_name):
    """Returns the type of file."""
    extension = file_name.lower().split('.')[-1]
    image_extensions = ['jpg', 'png', 'gif']
    video_extensions = ['mp3', 'mp4', 'mov', 'aae']
    if extension in image_extensions:
        return "Image"
    elif extension in video_extensions:
        return "Video"
    else:
        return "Other"

def is_vsco(image_exif):
    """Is this image taken with VSCO Cam?"""
    return image_exif['Software'] == 'VSCO'

def shot_with_iphone(image_exif):
    """Is this image shot with iPhone?"""
    if 'iPhone' in image_exif['LensModel']:
        return True

def is_normal_camera(image_exif):
    """Is this image shot with an iPhone, but not with VSCO?"""
 
FOLDER_PATH = os.path.expanduser("~/Pictures/Phone/")
IMAGE_FILE_NAMES = [f for f in os.listdir(FOLDER_PATH) if os.path.isfile(FOLDER_PATH + f)]

file_name = IMAGE_FILE_NAMES[1]
image_path = FOLDER_PATH + file_name

image_file_format = get_file_format(image_path)

if image_file_format == 'Image':
    image = Image.open(image_path)
    exif = {
    ExifTags.TAGS[k]: v
    for k, v in image._getexif().items()
    if k in ExifTags.TAGS
    }

