# iterate over files
# check if article exists
# if not then put file and desc to template
# save file in contend dir
import utils
from termcolor import colored

lacking = []

def render_file(code_number, code_title, file_name):
    code_first_digit = int(code_number / 100)

    return f"""---
title: {code_title}
code: {code_number}
description: {code_title}
category: {code_first_digit}xx
tags:
  - {code_first_digit}xx
pubDate: 2014-06-01
cover:  '../../assets/capy-media/{file_name}'
coverAlt: {code_title}
---

__DESCRIPTION__"""

for (code) in utils.codes:
    pattern = utils.pattern_for_code(code)
    match = 0
    file_name = ''
    for file in utils.files:
        if pattern.match(file):
            match += 1
            file_name = file
    if match != 1:
        print(colored(f"Wrong matches for {code[0]}", 'red'))
        lacking.append(str(code[0]))
        break;

    print(colored(f"OK {code[0]} {match}", 'green') + f" [{utils.get_size(file_name)/1e6}]")    # break

    print(render_file(code[0], code[1], file_name))
    fh = open(utils.base_content_dir + '/' + str(code[0]) + '.md', 'w')
    fh.write(render_file(code[0], code[1], file_name))


    print("")
