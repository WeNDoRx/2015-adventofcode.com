import re

pattern = re.compile(r"(-?(\d)+)")

with open('day12.input', 'r') as f:
    inp = f.readline().rstrip("\n")
    total = 0

    matches = re.findall(pattern, inp)
    for i in xrange(0, len(matches)):
        total += int(matches[i][0])

    print total