import re


pattern4 = re.compile(r".*(..).*\1.*")
pattern5 = re.compile(r".*(.).\1.*")

total_part_2 = 0

with open("day5.input") as f:
    for line in f:
    	string = line.replace('\n', '')
    	if pattern4.match(string) and pattern5.match(string):
    		total_part_2 += 1

print total_part_2