'''
Bruteforce all the way !
'''

from itertools import permutations

ingredients = {}

CAPACITY   = 2
DURABILITY = 4
FLAVOR     = 6
TEXTURE    = 8
CALORIES   = 10
INGREDIENTS_NR = 0

# http://mathoverflow.net/a/9494
def multichoose(n,k):
    if k < 0 or n < 0: return "Error"
    if not k: return [[0]*n]
    if not n: return []
    if n == 1: return [[k]]
    return [[0]+val for val in multichoose(n-1,k)] + \
        [[val[0]+1]+val[1:] for val in multichoose(n,k-1)]

# why ? beacuse it's a small imput and it' easyer to write a
# bruteforce algorithm than to write something useful lol
def bruteforce():
	max_score = 0
	# generate all possible quantities that sum up to 100
	quantities = multichoose(INGREDIENTS_NR, 100)
	# itterate through those quantities of form (cups_ingredient_1, cups_ingredient_2, ...)
	for cups in quantities:
		# initialise following variables with 0
		# ingredient_nr is the number of the current ingredient in the possible quantities
		score, capacity, durability, flavor, texture, ingredient_nr = (0,)*6
		# for each ingredient in the dictionary of ingredients
		for ingredient in ingredients:
			# calculate its different attributes
			capacity += cups[ingredient_nr] * ingredients[ingredient][0]
			durability += cups[ingredient_nr] * ingredients[ingredient][1]
			flavor += cups[ingredient_nr] * ingredients[ingredient][2]
			texture += cups[ingredient_nr] * ingredients[ingredient][3]
			# increment ingredient_nr so we multiply with the next ingredient in the list
			ingredient_nr += 1

		# calculate the score of the current configuration (nr of cups of each ingredient)
		score = capacity * durability * flavor * texture
		# but if any attribute < 0, score = 0
		if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
			score = 0

		max_score = max(max_score, score)

	print max_score

# first we read the ingredients in a dictionary of form
# 'IngredientName' : (capacity, durability, flavor, texture)
with open("day15.input") as f:
	for line in f:
		line = line.replace('\n', '')

		split = line.split(" ")
		ingredient = split[0][:-1]
		capacity   = int(split[CAPACITY][:-1])
		durability = int(split[DURABILITY][:-1])
		flavor     = int(split[FLAVOR][:-1])
		texture    = int(split[TEXTURE][:-1])
		calories   = int(split[CALORIES])

		ingredients[ingredient] = capacity, durability, flavor, texture
		INGREDIENTS_NR += 1

bruteforce()