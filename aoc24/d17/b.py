#a = 61657405
program = [2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0]

#a = int("1010",2)
#a = int("110111101101111",2)
#a = 12045678
#print(a)
#print(int("111",2))
b = 0
c = 0

p = 0

#a = 2024
#program = [0,1,5,4,3,0]

def combo(op,a,b,c):
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


def doprogram(a):
    program = [2,4,1,2,7,5,4,3,0,3,1,7,5,5,3,0]
    b = 0
    c = 0
    p = 0
    output = []
    while p < len(program):
        opcode = program[p]
        data = program[p+1]
        #print(p)
        #print(opcode,data)

        if opcode == 0:
            num = a
            den = pow(2,combo(data,a,b,c))
            a = int(num/den)
            p += 2
        elif opcode == 1:
            b = b ^ data
            p += 2
        elif opcode == 2:
            b = combo(data,a,b,c) % 8
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
            output.append(combo(data,a,b,c) % 8)
            p += 2
        elif opcode == 6:
            num = a
            den = pow(2,combo(data,a,b,c))
            b = int(num/den)
            p += 2
        elif opcode == 7:
            num = a
            den = pow(2,combo(data,a,b,c))
            c = int(num/den)
            p += 2
    return output

#a = int("5322353701101",8)
#print(doprogram(a))
#input()

#print(doprogram(int("5",8)))
#input()

attempts = ["5"]

for digit in range(1,16):
    nextattempts = []
    for i in range(8):
        for attempt in attempts:
            nextattempts.append(attempt + str(i))
    print(nextattempts)
    nextnextattempts = []
    for att in nextattempts:
        res = doprogram(int(att,8))
        good = True
        for d in range(1,digit+2):
            if res[-d] != program[-d]:
                good = False
        if good:
            nextnextattempts.append(att)
    print(nextnextattempts)
    attempts = nextnextattempts
    #input()
print(int(min(attempts),8))
