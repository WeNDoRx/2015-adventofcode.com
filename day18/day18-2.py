lights = []

def set_corner_lights():
	global lights
	lights[1][1] = '#'
	lights[1][len(lights[0]) - 2] = '#'
	lights[len(lights[0]) - 2][1] = '#'
	lights[len(lights[0]) - 2][len(lights[0]) - 2] = '#'

def count_neighbours(x, y):
	on = 0
	for x_t in xrange(x - 1, x + 2):
		for y_t in xrange(y - 1, y + 2):
			if lights[x_t][y_t] == '#':
				on += 1
	if lights[x][y] == '#':
		on += -1
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
set_corner_lights()

for x in xrange(0,100):
	update()
	set_corner_lights()

print sum(x.count('#') for x in lights)