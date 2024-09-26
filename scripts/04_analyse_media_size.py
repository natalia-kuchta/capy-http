import utils
from termcolor import colored

max_w = 0
min_w = 1e9
avg_w = 0
sum_w = 0

max_h = 0
min_h = 1e9
sum_h = 0

max_s = 0
min_s = 1e9
sum_s = 0

index = 0

exts = {}

for [code, title, file_name, extension] in utils.list_file_and_extensions_for_codes():

    # fh = open(utils.base_content_dir + '/' + str(code[0]) + '.md', 'w')
    [w, h] = utils.get_resolution(file_name, extension)

    if exts.get(extension):
        exts[extension] = exts.get(extension) + 1
    else:
        exts[extension] = 1

    size = utils.get_size(file_name)/1e6

    print(
        colored(f"OK {str(code)} {file_name}", 'green')
        + f"\tsiz = {size:5.2f} MB"
        + f"\tres = {w:5.0f} x {h:5.0f}"
    )

    max_w = max_w if max_w > w else w
    min_w = min_w if min_w < w else w
    sum_w += w

    max_h = max_h if max_h > h else h
    min_h = min_h if min_h < h else h
    sum_h += h

    max_s = max_s if max_s > size else size
    min_s = min_s if min_s < size else size
    sum_s += size


    index += 1

avg_w = sum_w / index
avg_h = sum_h / index
avg_s = sum_s / index

print(f"min_w = {min_w:5.0f}\tmax_w = {max_w:5.0f}\tavg_w = {avg_w:5.0f}\t")
print(f"min_h = {min_h:5.0f}\tmax_h = {max_h:5.0f}\tavg_h = {avg_h:5.0f}\t")
print(f"min_s = {min_s:5.0f}\tmax_s = {max_s:5.0f}\tavg_s = {avg_s:5.0f}\t")
print(f"computed for {index} elements")
print(exts)