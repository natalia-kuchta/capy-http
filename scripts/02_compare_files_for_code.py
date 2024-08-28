import utils
from termcolor import colored

for (code) in utils.codes:
    pattern = utils.pattern_for_code(code)
    matched = []
    for file in utils.files:
        if pattern.match(file):
            matched.append((code[0], file))
    if len(matched) > 1:
        print(colored(f"OK {code[0]} {len(matched)}", 'green'))
        for [code, file] in matched:
            print(f"{code} - [{utils.get_size(file)/1e6}] - {file}")

        print("")

