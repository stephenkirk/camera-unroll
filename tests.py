from main import *

assert get_tags_for_file(get_full_path(ex_screenshot)) == ['Image', 'Screenshot']
# assert get_tags_for_file(get_full_path(ex_snapchat_screenshot)) == ['Image', 'Screenshot', 'Snapchat']

get_tags_for_file(get_full_path(ex_snapchat_image))
get_tags_for_file(get_full_path(ex_glitche))
get_tags_for_file(get_full_path(ex_compressed_meme))
get_tags_for_file(get_full_path(ex_regular_video))
get_tags_for_file(get_full_path(ex_snapchat_screenshot))
get_tags_for_file(get_full_path(ex_snapchat_video))
get_tags_for_file(get_full_path(ex_vsco))


# TODO: Needs to return T
is_snapchat(get_image_exif(Image.open(get_full_path(ex_snapchat_image))))