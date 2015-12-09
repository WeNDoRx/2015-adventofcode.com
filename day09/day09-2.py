import networkx as nx
from itertools import permutations

G = nx.Graph()

# returns the weight between one city and another if any
def weight(one, other):
    ind = [i for i, v in enumerate(G.edges(data='weight')) if (v[0] == one and v[1] == other) or (v[0] == other and v[1] == one)]
    if ind != []:
     	return G.edges(data='weight')[ind[0]][2]

# why ? beacuse it's a small imput and it' easyer to write a
# bruteforce algorithm than to write the whole TSP algorithm
def bruteforce():
	max_yet = 0
	nodes_permutations = permutations(G.nodes())
	for route in nodes_permutations:
		length = 0
		current_city_index = 0
		# go through the route
		while current_city_index < len(route) - 1:
			# weigth between current city and next city
			w_c_n = weight(route[current_city_index], route[current_city_index+1])
			if w_c_n == None:
				length = 0
				break
			else:
				length += w_c_n
			current_city_index += 1

		max_yet = max(max_yet, length)
	print max_yet

with open("day9.input") as f:
    for line in f:
        line = line.replace('\n', '')

        split = line.split("=")
        from_to = split[0].split("to")

        from_node, to_node = from_to[0][:-1], from_to[1][1:-1]
        d = int(split[1])

        G.add_node(from_node)
        G.add_node(to_node)
        G.add_edge(from_node, to_node, weight=d)

bruteforce()