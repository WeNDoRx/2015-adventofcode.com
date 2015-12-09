import re

pattern1 = re.compile(".*[aeiou].*[aeiou].*[aeiou].*")
pattern2 = re.compile(r".*(.)\1.*")
pattern3 = re.compile("^((?!ab)(?!cd)(?!pq)(?!xy).)*$")

total_part_1 = 0

with open("day05.input") as f:
    for line in f:
    	string = line.replace('\n', '')
    	if pattern1.match(string) and pattern2.match(string) and pattern3.match(string):
    		total_part_1 += 1

print total_part_1