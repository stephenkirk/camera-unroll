"""aaah"""
import os
from PIL import Image
from PIL import ExifTags
import numpy as np

# Constants
FOLDER_PATH = os.path.expanduser("~/Pictures/Phone/")
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


def get_file_format(file_name):
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
    return shot_with_iphone(image_exif) and not is_vsco(image_exif)


def extract_vsco_filter(image_exif):
    try:
        split_comment = image_exif['UserComment'].decode("utf-8").split(" ")
        return split_comment[split_comment.index("preset")-1].upper() # Index before 'preset' is filter name
    except:
        return None

def is_screenshot(image):
    screenshot_resolutions = (1242, 2208), (2208, 1242), \
                             (750, 1334), (1334, 750), \
                             (640, 1136), (1136, 640), \
                             (640, 960), (960, 640)

    return(image.size in screenshot_resolutions)



def get_image_exif(image):
    exif = {
        ExifTags.TAGS[k]: v
        for k, v in image._getexif().items()
        if k in ExifTags.TAGS
    }
    return exif


def get_tags_for_file(file_name):
    file_type = get_file_format(file_name)
    tags = list()
    tags.append(file_type[0])
    if file_type[0] == 'Image':
        image = Image.open(file_name)
        if file_type[1] == 'jpg':
            exif = get_image_exif(image)
            if is_vsco(exif):
                tags.append("VSCO")
                tags.append(extract_vsco_filter(exif))
        elif file_type[1] == 'png':
            if is_screenshot(image): tags.append('Screenshot')
    return tags

# tag_dict = dict()
# num_files = enumerate(FILE_NAMES)

#for index, file_name in num_files:
#    full_file_path = FOLDER_PATH + file_name
#    tags = get_tags_for_file(full_file_path)
#    tag_dict[file_name] = tags
#    print('Scanning image ' + str(index) + '/' + str(len(FILE_NAMES)))

get_tags_for_file(FOLDER_PATH + ex_screenshot)