import utils
from termcolor import colored

lacking = []

for (code) in utils.codes:
    pattern = utils.pattern_for_code(code)
    match = 0
    last_matching_file = ''
    for file in utils.files:
        print("file", file)
        if pattern.match(file):
            match += 1
            print(f"{code[0]} - {file}")
            last_matching_file = file
    if match > 0:
        print(colored(f"OK {code[0]} {match}", 'green') + f" [{utils.get_size(last_matching_file)/1e6}]")
    else:
        print(colored(f"NO {code[0]}", 'red'))
        lacking.append(str(code[0]))
    print("")

if lacking:
    print(colored(f"Lacking: {', '.join(lacking)}", 'red'))
else:
    print(colored(f"All images collected", "green"))
