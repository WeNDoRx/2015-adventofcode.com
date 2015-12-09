'''
This one is a little trickyer so:
We have a dict that stores gates of form [input1, input2, operand, result]
so each gate is stored in the dict by its name as the dict key and as value
the list [input1, input2, operand result]. Now, we first read the circuit
with the read_circuit() function. Then, we check what gates already have all
the required informations (inpot1 and input2). For the gates we find to have
all necessary information, we propagate their value through the circuit and
delete the gate from the dict. We then proceed to update the circuit. Updating
the circuit means we calculate the result of the gates we have the required
inputs and store them in result. Then we propagate, update, propagate, update
and so on untill gate 'a' has a result and save the result. We then repeat
the whole process but after we read the circuit we set the value of b to the
previous value of a, as required by the challenge.
'''

# circuit holds gates of form [input1, input2, operand result]
circ = {}

def read_circuit():
# read input
    with open("day07.input") as f:
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

# print circuit (for debug)
def print_circuit():
    for k, v in circ.items():
        print (k, '-->', v)

# substitute a gate's value in the circuit where
def substitute(gate, gate_value):
    for key, value in circ.iteritems():
        if value[0] == gate:
            circ[key][0] = gate_value
        if value[1] == gate:
            circ[key][1] = gate_value

# update the circuit
def update_circ():
    for key, value in circ.iteritems():
        if str(value[0]).isdigit() and str(value[1]).isdigit():
            update_value(key)

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

# read circuit from file
read_circuit()
# unless we found the value of a
while circ['a'][3] == None:
    # for all values in dict, if the gate has been computed
    for key, value in circ.iteritems():
        if value[3] != None:
            # proagate its value
            substitute(key, value[3])
            # remove the gate key from the circuit since it's value has been substituted everywhere
            circ = {i:circ[i] for i in circ if i!=key}
    # update circuit
    update_circ()

# now print the value of gate a so we save it
saved = circ['a'][3]

read_circuit()
circ['b'][0] = saved
# unless we found the value of a
while circ['a'][3] == None:
    # for all values in dict, if the gate has been computed
    for key, value in circ.iteritems():
        if value[3] != None:
            # proagate its value
            substitute(key, value[3])
            # remove the gate key from the circuit since it's value has been substituted everywhere
            circ = {i:circ[i] for i in circ if i!=key}
    # update circuit
    update_circ()

print circ['a'][3]