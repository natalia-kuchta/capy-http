import os.path

import utils

import cv2
import PIL
from PIL import Image, ImageOps, ImageSequence
import numpy as np

target_width = 750
target_height = 600

def resize_jpeg_by_open_cv(code, title, file, ext):
    if ext == '.jpg':
        target_file_name = utils.base_target_dir + '/' + str(code) + '_750x600' + ext
        if os.path.exists(target_file_name):
            return
        image = cv2.imread(utils.base_media_dir + '/' + file)
        orig_height, orig_width = image.shape[:2]
        orig_aspect = orig_width / orig_height
        target_aspect = target_width / target_height
        if orig_aspect > target_aspect:
            new_width = target_width
            new_height = int(target_width / orig_aspect)
        else:
            new_height = target_height
            new_width = int(target_height * orig_aspect)
        resized_image = cv2.resize(image, (new_width, new_height))
        result_image = np.zeros((target_height, target_width, 3), dtype=np.uint8)
        x_offset = (target_width - new_width) // 2
        y_offset = (target_height - new_height) // 2
        result_image[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_image
        cv2.imwrite(target_file_name, result_image)

def resize_webp_by_pillow(code, title, file, ext):
    if ext == '.webp' or ext == '.gif':
        target_file_name = utils.base_target_dir + '/' + str(code) + '_750x600' + ext
        if os.path.exists(target_file_name):
            return

            # Open the image
        image = Image.open(utils.base_media_dir + '/' + file)

        # Check if the image is animated
        if getattr(image, "is_animated", False):
            frames = []
            for frame in ImageSequence.Iterator(image):
                # Get the original dimensions of the frame
                orig_width, orig_height = frame.size

                # Calculate the aspect ratios
                orig_aspect = orig_width / orig_height
                target_aspect = target_width / target_height

                if orig_aspect > target_aspect:
                    # If the image is too wide, resize based on the width
                    new_width = target_width
                    new_height = int(target_width / orig_aspect)
                else:
                    # Otherwise, resize based on the height
                    new_height = target_height
                    new_width = int(target_height * orig_aspect)

                # Resize the frame while maintaining aspect ratio
                resized_frame = frame.resize((new_width, new_height), Image.ANTIALIAS)

                # Create a black background canvas with the target dimensions
                result_frame = Image.new('RGBA', (target_width, target_height), (0, 0, 0, 255))

                # Calculate the top-left corner where the image should be placed on the canvas
                x_offset = (target_width - new_width) // 2
                y_offset = (target_height - new_height) // 2

                # Paste the resized frame onto the black canvas
                result_frame.paste(resized_frame, (x_offset, y_offset))

                # Append the processed frame to the list
                frames.append(result_frame)

            # Save the frames as a new animated WebP
            frames[0].save(
                target_file_name,
                save_all=True,
                append_images=frames[1:],
                duration=image.info['duration'],
                loop=image.info.get('loop', 0)
            )

        else:
            # If the image is not animated, process it normally
            orig_width, orig_height = image.size

            # Calculate the aspect ratios
            orig_aspect = orig_width / orig_height
            target_aspect = target_width / target_height

            if orig_aspect > target_aspect:
                # If the image is too wide, resize based on the width
                new_width = target_width
                new_height = int(target_width / orig_aspect)
            else:
                # Otherwise, resize based on the height
                new_height = target_height
                new_width = int(target_height * orig_aspect)

            # Resize the image while maintaining aspect ratio
            resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

            # Create a black background canvas with the target dimensions
            result_image = Image.new('RGBA', (target_width, target_height), (0, 0, 0, 255))

            # Calculate the top-left corner where the image should be placed on the canvas
            x_offset = (target_width - new_width) // 2
            y_offset = (target_height - new_height) // 2

            # Paste the resized image onto the black canvas
            result_image.paste(resized_image, (x_offset, y_offset))

            # Save the final image
            result_image.save(target_file_name, image.format)


for [code, title, file, ext] in utils.list_file_and_extensions_for_codes():
    print(f"code: {code}, ext: {ext}")
    resize_jpeg_by_open_cv(code, title, file, ext)
    resize_webp_by_pillow(code, title, file, ext)


    # if ext == '.jpg':
    #     image = cv2.imread(utils.base_media_dir + '/' + file)
    #     resized_image = cv2.resize(image, (target_width, target_height))
    #     cv2.imwrite(utils.base_target_dir + '/' + str(code) + '_750x600' + ext, resized_image)

    # if ext == '.mp4':
    #     vid = cv2.VideoCapture(base_media_dir + '/' + file)
    #     hgt = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #     wid = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    #     return wid, hgt
    #
    # img = PIL.Image.open(base_media_dir + '/' + file)
    # wid, hgt = img.size
    # return wid, hgt