import md5

with open('day4.input', 'r') as f:
    my_hash = f.readline().rstrip("\n")

# i is the number that is added at the end
# f and s are bools for found five and 6 first digits == 0
i, f, s = 0, 0, 0

while f + s < 2:
	if f == 0:
		m = md5.new()
		m.update(my_hash+str(i))
		if m.hexdigest()[:5] == "00000":
		 	print "index:", i, "hash:", m.hexdigest()
		 	f = 1
	if s == 0:
		m = md5.new()
		m.update(my_hash+str(i))
		if m.hexdigest()[:6] == "000000":
			print "index:", i, "hash:", m.hexdigest()
			s = 1
	
	i += 1