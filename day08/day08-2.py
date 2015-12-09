import re

len_read = 0
len_code = 0

# read input
with open("day8.input") as f:
    for line in f:
        line = line.replace('\n', '')
        len_read += len(line)

        # replace \ with \\ in the string
        line = re.sub(r'\\', r'\\\\', line)
        # replace " with \" in the string
        line = re.sub(r'"', r'\\"', line)

        # coun the surrounding brackets
        len_code += len(line) + 2

print len_code - len_read