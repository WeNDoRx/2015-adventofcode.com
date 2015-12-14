# analytical solution because it's nicer

race_end = 2503

max_dist = 0

# for all reindeers calculate how much they flew
with open("day14.input") as f:
	for line in f:
		line = line.replace('\n', '')

		split = line.split(" ")
		
		fly_speed = int(split[3])
		fly_time = int(split[6])
		rest_time = int(split[-2])

		# it goes like race_end modulo fly_time + rest_time
		# and the whole part gets multiplied
		i, d = divmod(race_end, fly_time + rest_time)

		# but with the rest, there are two options
		# either he got to fly a whole run and is resting at
		# the time the race ends
		if d >= fly_time:
			rest_distance = fly_time * fly_speed
		# or he is racing at the time the race ends
		else:
			rest_distance = d * fly_speed

		flew = (fly_speed * fly_time) * i + rest_distance

		max_dist = max(max_dist, flew)

print max_dist