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

gatelist = defaultdict(list)

for gate in gates.strip().split("\n"):
    gate = gate.split()
    inp1 = gate[0]
    inp2 = gate[2]
    ins = gate[1]
    out = gate[4]
    gatelist[(inp1,inp2)].append([ins,out])



wires = {}

#badbits = ["04","05","10","14","15","29","30"]
badbits = ["00","01","02","03","04","05"]
for bit in badbits:
    relevantgates = ["x"+bit, "y"+bit]
    loopagain = True
    while loopagain:
        loopagain = False
        for gate in gatelist:
            if gate[0] in relevantgates or gate[1] in relevantgates:
                print(gatelist[gate])
                for out in gatelist[gate]:
                    relevantgates.append(out[1])
                loopagain == True
    print(relevantgates)

