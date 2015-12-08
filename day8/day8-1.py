import re

len_code = 0
len_in_mem = 0

# read input
with open("day8.input") as f:
    for line in f:
        line = line.replace('\n', '')
        len_code += len(line)
        # replace \\ with | in the string
        line = re.sub(r'\\{2}', '|', line)
        # replace \" with " in the string
        line = re.sub(r'\\\"', '"', line)
        # replace \x hex representations with a character
        line = re.sub(r'\\x[0-9a-fA-F]{2}', '|', line)
        len_in_mem += len(line) - 2
        print line, len(line) - 2

print len_code, "-", len_in_mem, "=", len_code - len_in_mem