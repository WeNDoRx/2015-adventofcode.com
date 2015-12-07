import re

pattern1 = re.compile(".*[aeiou].*[aeiou].*[aeiou].*")
pattern2 = re.compile(r".*(.)\1.*")
pattern3 = re.compile("^((?!ab)(?!cd)(?!pq)(?!xy).)*$")

pattern4 = re.compile(r".*(..).*\1.*")
pattern5 = re.compile(r".*(.).\1.*")

total_part_1 = 0
total_part_2 = 0

with open("day5.input") as f:
    for line in f:
    	string = line.replace('\n', '')
    	if pattern1.match(string) and pattern2.match(string) and pattern3.match(string):
    		total_part_1 += 1
    	if pattern4.match(string) and pattern5.match(string):
    		total_part_2 += 1

print total_part_1, total_part_2