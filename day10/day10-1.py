import re

with open('day10.input', 'r') as f:
    inp = f.readline().rstrip("\n")

    runs = 40

    while runs > 0:
    	new = ""
    	while inp != "":
    		tmp = len(re.search(r"(.)\1*", inp).group())
    		new += str(tmp) + inp[0]
    		inp = inp[tmp:]
    	inp = new
    	runs += -1
print len(inp)