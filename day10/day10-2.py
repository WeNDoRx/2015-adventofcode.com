# this shit solution takes like forever !
# ... more like 10 minutes ... but that's like forever !
# this is most probably due the many assignments ...

import re

with open('day10.input', 'r') as f:
    inp = f.readline().rstrip("\n")

    runs = 50

    while runs > 0:
    	new = ""
    	while inp != "":
    		tmp = len(re.search(r"(.)\1*", inp).group())
    		new += str(tmp) + inp[0]
    		inp = inp[tmp:]
    	inp = new
    	runs += -1
print len(inp)