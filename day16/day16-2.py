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
				# if we're talking about the attributes "cats" and "trees"
				if detectable_attributes.index(attribute) == 1 or detectable_attributes.index(attribute) == 7:
					# if the quantity detected is more than the quantity from the sample, increment the found counter
					if int(split[index + 1]) > detected_quantities[detectable_attributes.index(attribute)]:
						found += 1
				# if we're talking about the attributes "pomeranians" and "goldfish"
				elif detectable_attributes.index(attribute) == 3 or detectable_attributes.index(attribute) == 6:
					# if the quantity detected is less than the quantity from the sample, increment the found counter
					if int(split[index + 1]) < detected_quantities[detectable_attributes.index(attribute)]:
						found += 1
				# in all other cases
				else:
					# if the quantity detected equals the quantity from the sample, increment the found counter
					if int(split[index + 1]) == detected_quantities[detectable_attributes.index(attribute)]:
						found += 1
		# if 3 attributes match
		if found == 3:
			print split[1]