'''
Bruteforce all the way ! This is fucked up. Good luck trying to understand
this. And good luck to me if I ever want to understand this again. Greetings
from your dickhead of a past yourself !
'''

from itertools import permutations

people = {}

# http://stackoverflow.com/a/8550942/986495
def addNameToDictionary(d, tup):
	if tup[0] not in d:
		d[tup[0]] = {}
	d[tup[0]][tup[1]] = tup[2]

# why ? beacuse it's a small imput and it' easyer to write a
# bruteforce algorithm than to write something useful lol
def bruteforce():
	max_love = 0
	arrangements_permutations = permutations(people.keys())
	for arrangements in arrangements_permutations:
		arrangements_list = list(arrangements)
		love = 0
		for x in xrange(1, len(arrangements_list)-1):
			love += people[arrangements_list[x]][arrangements_list[x-1]] + people[arrangements_list[x]][arrangements_list[x+1]]
		love += people[arrangements_list[0]][arrangements_list[len(arrangements_list)-1]] + people[arrangements_list[0]][arrangements_list[1]]
		love += people[arrangements_list[len(arrangements_list)-1]][arrangements_list[len(arrangements_list)-2]] + people[arrangements_list[len(arrangements_list)-1]][arrangements_list[0]]
		max_love = max(max_love, love)
	print max_love

with open("day13.input") as f:
	for line in f:
		line = line.replace('\n', '')

		split = line.split(" ")
		who = split[0]
		next_to = split[-1:][0][:-1]
		amount = int(split[3])
		if split[2] == "lose":
			amount *= -1
		addNameToDictionary(people, (who, next_to, amount))
		# add myself to the table
		for key in people.keys():
			addNameToDictionary(people, ("me", key, 0))
			addNameToDictionary(people, (key, "me", 0))

bruteforce()