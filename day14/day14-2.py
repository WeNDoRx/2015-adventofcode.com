race_end = 2503
reindeers = {}
max_dist = 0

def flew_until_now(fly_speed, fly_time, rest_time, time_passed_until_now):
	i, d = divmod(time_passed_until_now, fly_time + rest_time)

	# but with the rest, there are two options
	# either he got to fly a whole run and is resting at
	# the time the race ends
	if d >= fly_time:
		rest_distance = fly_time * fly_speed
	# or he is racing at the time the race ends
	else:
		rest_distance = d * fly_speed

	return (fly_speed * fly_time) * i + rest_distance

# reading the reindeers from the file into the dictionary
with open("day14.input") as f:
	for line in f:
		line = line.replace('\n', '')

		split = line.split(" ")

		name = split[0]
		fly_speed = int(split[3])
		fly_time = int(split[6])
		rest_time = int(split[-2])
		# dictionary is of form d[k] = [fly_speed, fly_time, rest_time, points_won]
		reindeers[name] = [fly_speed, fly_time, rest_time, 0]

# we simulate the race
for x in xrange(1,race_end):
	temp_max_dist = 0
	# this holds the raindeers who are leading the race
	temp_reindeer = []
	# for all reindeers
	for key in reindeers:
		temp_speed = reindeers[key][0]
		temp_time = reindeers[key][1]
		temp_rest = reindeers[key][2]
		# if their calculated distance is treater than the temporary max distance
		if flew_until_now(temp_speed, temp_time, temp_rest, x) > temp_max_dist:
			# update the temporary max distance and the list that holds the temporary leaders
			temp_max_dist = flew_until_now(temp_speed, temp_time, temp_rest, x)
			temp_reindeer = [key]
		# if the distance equals the temporary max distance, add the reindeer to the list of leaders
		elif flew_until_now(temp_speed, temp_time, temp_rest, x) == temp_max_dist:
				temp_reindeer += [key]

	# increase the points of the reindeer that are in the lead
	for top_raindeers in temp_reindeer:
		reindeers[top_raindeers][3] += 1

# print the leader's points
print max(l[3] for l in reindeers.itervalues())