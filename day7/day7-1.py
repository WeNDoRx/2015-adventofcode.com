# circuit holds gates of form [input1, input2, operand result]
circ = {}

# print circuit (for debug)
def print_circuit():
    for k, v in circ.items():
        print (k, '-->', v)

# substitute a value in the circuit
def substitute(key, value):
    for keyx, valuex in circ.iteritems():
        if valuex[0] == key:
            circ[keyx][0] = value
        if valuex[1] == key:
            circ[keyx][1] = value

# update a gates value
def update_value(key):
    if circ[key][2] == "and":
        circ[key][3] = int(circ[key][0]) & circ[key][1]
    if circ[key][2] == "or":
        circ[key][3] = circ[key][0] | circ[key][1]
    if circ[key][2] == "lsh":
        circ[key][3] = circ[key][0] << circ[key][1]
    if circ[key][2] == "rsh":
        circ[key][3] = circ[key][0] >> circ[key][1]
    if circ[key][2] == "not":
        circ[key][3] = circ[key][0] ^ 65535

# update the circuit
def update_circ():
    for key, value in circ.iteritems():
        if str(value[0]).isdigit() and str(value[1]).isdigit():
            update_value(key)

# read input
with open("day7.input") as f:
    for line in f:
        line = line.replace('\n', '').split(" ")
        
        # get source
        s = line[-1:][0]
        
        # find location of "->" so we cand deduce the operation
        operation = line.index("->")
        
        # if operation == 1 then we have assignment
        if operation == 1:
            circ[s] = [line[0], 65535, "and", None]
            if line[0].isdigit():
                circ[s][0] = int(line[0])

        # if operation == 2 we have inversion of bits
        elif operation == 2:
            circ[s] = [line[1], 0, "not", None]

        # else we have AND, OR, LSHIFT or RSHIFT
        else:
            # opcode differenteiates between AND, OR, LSHIFT or RSHIFT
            opcode = line[1][0]
            if opcode == "A":
                circ[s] = [line[0], line[2], "and", None]
            elif opcode == "O":
                circ[s] = [line[0], line[2], "or", None]
            elif opcode == "L":
                circ[s] = [line[0], int(line[2]), "lsh", None]
            else:
                circ[s] = [line[0], int(line[2]), "rsh", None]

# unless we found the value of a
while circ['a'][3] == None:
    # for all values in dict, if the gate has been computed
    for key, value in circ.iteritems():
        if value[3] != None:
            # proagate its value
            substitute(key, value[3])

    # update circuit
    update_circ()

# now print the value of gate a
print circ['a'][3]