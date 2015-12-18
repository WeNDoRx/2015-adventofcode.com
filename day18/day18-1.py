from pprint import pprint
import copy

lights = []

def count_neighbours(x, y):
	on = 0
	if lights[x+1][y] == '#':
		on += 1
	if lights[x][y+1] == '#':
		on += 1
	if lights[x-1][y] == '#':
		on += 1
	if lights[x][y-1] == '#':
		on += 1
	if lights[x+1][y+1] == '#':
		on += 1
	if lights[x-1][y-1] == '#':
		on += 1
	if lights[x-1][y+1] == '#':
		on += 1
	if lights[x+1][y-1] == '#':
		on += 1
	return on

def update():
	global lights
	new = [x[:] for x in [['.']*len(lights[0])]*len(lights[0])]
	for x in xrange(1,len(lights[0]) - 1):
		for y in xrange(1,len(lights[0]) - 1):
			neighbours_on = count_neighbours(x,y)
			if lights[x][y] == '#':
				if neighbours_on == 2 or neighbours_on == 3:
					new[x][y] = '#'
				else:
					new[x][y] = '.'
			if lights[x][y] == '.':
				if neighbours_on == 3:
					new[x][y] = '#'
				else:
					new[x][y] = '.'
	lights = new

f = open ( 'day18.input' , 'r')
lights = [ list(line.replace('\n', '')) for line in f ]

lights = [['.'] * len(lights[0])] + lights + [['.'] * len(lights[0])]
lights = [['.'] + row + ['.'] for row in lights]

for x in xrange(0,100):
	update()

print sum(x.count('#') for x in lights)