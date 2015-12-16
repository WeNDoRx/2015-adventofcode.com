# this problem should have been done with constraints programming. but meh ...

detectable_attributes = ["children", "cats", "samoyeds", "pomeranians", "akitas", "vizslas", "goldfish", "trees", "cars", "perfumes"]
detected_quantities = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]

with open("day16.input") as f:
	for line in f:
		split = line.replace('\n', '').replace(',', '').replace(':', '').split(" ")
		# how many of the attributes were identified and are present here
		found = 0
		# for all atributes that were detected 
		for attribute in detectable_attributes:
			# if there was an attribute detected
			if attribute in split:
				# location of that attribute in the line
				index = split.index(attribute)
				# if the detected attribute quantity == the quantity of the probing sample
				if int(split[index + 1]) == detected_quantities[detectable_attributes.index(attribute)]:
					# increment the counter that says how many attributes match
					found += 1
		# if 3 attributes match
		if found == 3:
			print split[1]