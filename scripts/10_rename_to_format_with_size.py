import utils
import glob
import os
from PIL import Image
import pillow_avif

files = [os.path.basename(file) for file in glob.glob(utils.base_official_dir + "/*")]
for file_name in files:
    old_path = f"{utils.base_official_dir}/{file_name}"
#     img = Image.open(old_path)

    extension = file_name.split('.')[-1]
    code = int(file_name.split('.')[0].replace('Capy', ''))
    new_name = f"Capy-{code}-750x600.{extension}"
    new_path = f"{utils.base_official_dir}/{new_name}"


#     img.save(new_path, save_all=True)
    os.rename(old_path, new_path)