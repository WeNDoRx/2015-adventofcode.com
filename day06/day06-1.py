import numpy

r = numpy.zeros(shape=(1000 ,1000))

with open("day6.input") as f:
    for line in f:
        split = line.replace('\n', '').split(" ")
        offset = 0
        operation = 0
        if split[0][1] == "u":
        	offset = 1
        if split[1][1] == "n":
        	operation = 1
        elif split[1][1] == "f":
        	operation = 2

        i_from, j_from = int(split[1+offset].split(',')[0]), int(split[1+offset].split(',')[1])
        i_to, j_to = int(split[3+offset].split(',')[0]), int(split[3+offset].split(',')[1])

        for x in xrange(i_from, i_to+1):
        	for y in xrange(j_from, j_to+1):
        		if operation == 1:
        			r[x][y] = 1
        		if operation == 2:
        			r[x][y] = 0
        		if operation == 0:
        			r[x][y] = not r[x][y]

print numpy.count_nonzero(r)