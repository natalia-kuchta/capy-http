import utils
import glob
import os
from PIL import Image
import pillow_avif

size = (250, 200)

# this script convert only webp
# bash convert for avif
# find ../src/assets/capy-official/ -name '*750x600*.avif' -exec sh -c '
#     for file; do
#         base="${file%.*}"
#         convert "$file" -resize 250x200 "${base%750x600}250x200.avif"
#     done
# ' sh {} +


def resize_animated_webp(input_path, output_path, size):
    with Image.open(input_path) as img:
        # Create an empty list to hold the resized frames
        frames = []

        # Iterate through each frame in the animated WebP
        for frame_index in range(0, img.n_frames):
            img.seek(frame_index)
            frame = img.copy()
            frame = frame.resize(size, Image.LANCZOS)
            frames.append(frame)

        # Save all frames as a new animated WebP
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0)


files = [os.path.basename(file) for file in glob.glob(utils.base_official_dir + "/*750x600.webp")]
for file_name in files:
    old_path = f"{utils.base_official_dir}/{file_name}"

    extension = file_name.split('.')[-1]
    code = int(file_name.split('.')[0].split('-')[1])
    new_name = f"Capy-{code}-250x200.{extension}"
    new_path = f"{utils.base_official_dir}/{new_name}"

    resize_animated_webp(old_path, new_path, size)

    print(new_path)
