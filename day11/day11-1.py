'''
I haven't slept last night. at all. I don't even know what I did here lol ...
'''

import re, sys

pattern = re.compile(r".*(.)\1.*!?(.)\2.*")

def next_string(old_string):
	old_string = list(old_string)
	old_string[-1:] = chr(ord(old_string[-1:][0]) + 1)

	for i in reversed(xrange(len(old_string))):
		if ord(old_string[i]) > 122:
			old_string[i] = chr(ord(old_string[i]) % 122 + 97 - 1)
			old_string[i-1] = chr(ord(old_string[i-1]) + 1)
	return ''.join(old_string)

with open('day11.input', 'r') as f:
    old_pass = f.readline().rstrip("\n")

i = 0
while i < 1:
	old_pass = next_string(old_pass)
	if old_pass.find('i') + old_pass.find('o') + old_pass.find('l') > -3:
		continue

	if not re.match(pattern, old_pass):
		continue

	for x in xrange(0, len(old_pass) - 2):
		if ord(old_pass[x]) == (ord(old_pass[x+1])-1) and ord(old_pass[x]) == (ord(old_pass[x+2])-2):
			print old_pass
			i += 1