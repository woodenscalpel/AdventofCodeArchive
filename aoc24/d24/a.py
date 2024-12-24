from collections import defaultdict
f = open("input.txt","r").read()

def op(in1,in2,operation):
    if operation == "AND":
        return in1 and in2
    if operation == "OR":
        return in1 or in2
    if operation == "XOR":
        return in1 ^ in2


initial,gates = f.split("\n\n")

#print(initial,gates)


wires = {}

for wire in initial.split("\n"):
    wire = wire.split(":")
    wires[wire[0]] = int(wire[1].lstrip())

print(wires)
gatelist = defaultdict(list)

for gate in gates.strip().split("\n"):
    gate = gate.split()
    inp1 = gate[0]
    inp2 = gate[2]
    ins = gate[1]
    out = gate[4]
    print(inp1,inp2,ins,out)
    gatelist[(inp1,inp2)].append([ins,out])


while gatelist:
    nextgates = {}
    for gate in gatelist:
        if(gate[0] in wires and gate[1] in wires):
            for output in gatelist[gate]:
                wires[output[1]] = op(wires[gate[0]],wires[gate[1]],output[0])
        else:
            nextgates[gate] = gatelist[gate]
    gatelist = nextgates

print(wires)

binstring = ""
for i in range(99):
    checkwire = "z" + str(i).zfill(2)
    if checkwire in wires:
        binstring += str(wires[checkwire])
    else:
        break
silver = int(binstring[::-1],2)
print(silver)


