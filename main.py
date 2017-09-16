"""aaah"""
import os
from PIL import Image
from PIL import ExifTags

# Constants
FOLDER_PATH = os.path.expanduser("~/Pictures/Phone/")
IMAGE_FILE_NAMES = [f for f in os.listdir(FOLDER_PATH) if os.path.isfile(FOLDER_PATH + f)]

# Example images
ex_compressed_meme = "IMG_3940 1.JPG"
ex_glitche = "IMG_3932.JPG"
ex_screenshot = "IMG_3931.PNG"
ex_snapchat_screenshot = "IMG_3922.PNG"
ex_snapchat_video = "RHYH3563.MP4"
ex_snapchat_image = "IMG_3903.JPG"
ex_regular_video = "IMG_3217.MOV"
ex_vsco = "JWBO4754.JPG"


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
    try: return image_exif['Software'] == 'VSCO'
    except: return False


def shot_with_iphone(image_exif):
    """Is this image shot with iPhone?"""
    if 'iPhone' in image_exif['LensModel']:
        return True


def is_normal_camera(image_exif):
    """Is this image shot with an iPhone, but not with VSCO?"""


def extract_tag(image_exif):
    split_comment = image_exif['UserComment'].decode("utf-8").split(" ")
    tags.append(split_comment[split_comment.index("preset")-1].upper())


def get_tags_for_file(file_name):
    file_path = FOLDER_PATH + file_name
    file_type = get_file_format(file_path)

    tags = []

    if file_type == 'Image':
        tags.append("Image")
        image = Image.open(file_path)
        exif = {
            ExifTags.TAGS[k]: v
            for k, v in image._getexif().items()
            if k in ExifTags.TAGS
        }
        if is_vsco(exif):
            tags.append("VSCO")
            tags.append(extract_tag(exif))


    return tags


# file_name = ex_vsco

get_tags_for_file(file_name=ex_snapchat_image)
