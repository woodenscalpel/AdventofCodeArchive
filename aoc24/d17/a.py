a = 61657405
program = [2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0]
b = 0
c = 0

p = 0

#a = 2024
#program = [0,1,5,4,3,0]

def combo(op):
    if op < 4:
        return op
    if op == 4:
        return a
    if op == 5:
        return b
    if op == 6:
        return c
    else:
        input()
        return -1


p = 0
output = []
while p < len(program):
    opcode = program[p]
    data = program[p+1]
    #print(p)
    #print(opcode,data)

    if opcode == 0:
        num = a
        den = pow(2,combo(data))
        a = int(num/den)
        p += 2
    elif opcode == 1:
        b = b ^ data
        p += 2
    elif opcode == 2:
        b = combo(data) % 8
        p += 2
    elif opcode == 3:
        if a != 0:
            p = data
        else:
            p += 2
    elif opcode == 4:
        b = b ^ c
        p += 2
    elif opcode == 5:
        output.append(combo(data) % 8)
        p += 2
    elif opcode == 6:
        num = a
        den = pow(2,combo(data))
        b = int(num/den)
        p += 2
    elif opcode == 7:
        num = a
        den = pow(2,combo(data))
        c = int(num/den)
        p += 2

print(output)
print(a)
