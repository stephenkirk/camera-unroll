def is_vsco(image_exif):
    """Is this image taken with VSCO Cam?"""
    try:
        return image_exif['Software'] == 'VSCO'
    except:
        return False

def shot_with_iphone(image_exif):
    """Is this image shot with iPhone?"""
    try:
        return 'iPhone' in image_exif['LensModel']
    except:
        return False

def is_normal_camera(image_exif):
    """Is this image shot with an iPhone, but not with VSCO?"""
    return shot_with_iphone(image_exif) and not is_vsco(image_exif)

def extract_vsco_filter(image_exif):
    """Get which VSCO filter was used, assuming it is a VSCO file."""
    try:
        split_comment = image_exif['UserComment'].decode("utf-8").split(" ")
        return split_comment[split_comment.index("preset") - 1].upper()  # Index before 'preset' is filter name
    except:
        return None

def is_snapchat(image_exif):
    try:
        return (not is_normal_camera(image_exif)) & \
                image_exif['ExifImageHeight'] in (1920, 1080) & \
                image_exif['ExifImageWidth'] in (1920, 1080)
    except:
        return False

def is_screenshot(image):
    screenshot_resolutions = (1242, 2208), (2208, 1242), \
                             (750, 1334), (1334, 750), \
                             (640, 1136), (1136, 640), \
                             (640, 960), (960, 640)
    return image.size in screenshot_resolutions




def get_image_exif(image):
    exif = {
        ExifTags.TAGS[k]: v
        for k, v in image._getexif().items()
        if k in ExifTags.TAGS
    }
    return exif

def get_full_path(image_path):
    return FOLDER_PATH + image_path

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
            if is_snapchat(exif):
                tags.append("Snapchat")
        elif file_type[1] == 'png':
            if is_screenshot(image): tags.append('Screenshot')
    return tags


mediainfo = subprocess.Popen(['mediainfo', get_full_path(ex_snapchat_video)],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)

# TODO: Insert this into a array or hashmap, so we can access values such as bit rate easily
for line in mediainfo.stdout:
    line_obj = line.decode("utf-8").split(':')
    key = line_obj[0].strip()
    print(line_obj.len) # Check the length here, if above 2 merge everything but first (as we performed an overzealous split)
    # print(key)


tag_dict = dict()
num_files = enumerate(FILE_NAMES[0:4999])
#
# for index, file_name in num_files:
#     full_file_path = FOLDER_PATH + file_name
#     tags = get_tags_for_file(full_file_path)
#     tag_dict[file_name] = tags
#     print('Scanning image ' + str(index) + '/' + str(len(FILE_NAMES)))