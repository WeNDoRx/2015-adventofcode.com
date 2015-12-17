from itertools import combinations

containers = []

with open("day17.input") as f:
	for line in f:
		containers.append(int(line))

print len([comb for i in range(1, len(containers)) for comb in combinations(containers, i) if sum(comb) == 150])