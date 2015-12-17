from itertools import combinations

containers = []

with open("day17.input") as f:
	for line in f:
		containers.append(int(line))

found, ind = 0, 0

while found == 0:
	found = len([comb for i in range(1, len(containers)) for comb in combinations(containers, i) if sum(comb) == 150 and len(comb) == ind])
	ind += 1

print found