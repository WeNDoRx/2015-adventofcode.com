f = open('day01.input')
line = f.readline()
i = 0
for x in xrange(0, len(line)):
	if line[x] == '(':
		i += 1
	else:
		i += -1
	if i < 0:
		print x + 1
		break