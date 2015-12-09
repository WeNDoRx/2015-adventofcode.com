import md5

with open('day04.input', 'r') as f:
    my_hash = f.readline().rstrip("\n")

i = 0

while True:
	m = md5.new()
	m.update(my_hash+str(i))
	if m.hexdigest()[:6] == "000000":
		print "index:", i, "hash:", m.hexdigest()
		break

	i += 1