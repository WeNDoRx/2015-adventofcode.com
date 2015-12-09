import numpy

with open ("day03.input", "r") as myfile:
    data=myfile.read().replace('\n', '')

r = numpy.zeros(shape=(20000 ,20000))

width = r.shape[0]
height = r.shape[1]

begin_x = 10000
begin_y = 10000

index = 0

while index < len(data):
	# increase presents dropped at cuurent location
	r[begin_x][begin_y] += 1
	# get direction
	drop = data[index]
	if drop == ">":
		begin_x += 1
	if drop == "<":
		begin_x += -1
	if drop == "^":
		begin_y += 1
	if drop == "v":
		begin_y += -1
	index += 2

begin_x = 10000
begin_y = 10000

index = 1

while index < len(data):
	# increase presents dropped at cuurent location
	r[begin_x][begin_y] += 1
	# get direction
	drop = data[index]
	if drop == ">":
		begin_x += 1
	if drop == "<":
		begin_x += -1
	if drop == "^":
		begin_y += 1
	if drop == "v":
		begin_y += -1
	index += 2

print numpy.count_nonzero(r)