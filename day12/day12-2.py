import re
import json

obj  = json.load(open("day12.input"))

def rec_sum(node):
	# if we have a dict
	if isinstance(node, dict):
		# return 0 if it contains red
		if "red" in node.values():
			return 0
		# call the function recursive on node values else and return the result
		else:
			return rec_sum(node.values())

	# if we have a list, return the sum of the recurison on all nodes
	elif isinstance(node, list):
		return sum([rec_sum(nodes) for nodes in node])

	# if we have an int, return it
	elif isinstance(node, int):
		return node

	# in all other cases, return 0
	return 0

print rec_sum(obj)