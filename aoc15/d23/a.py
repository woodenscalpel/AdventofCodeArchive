lines = open("input.txt","r").readlines()

lines  = [[x.strip(",").strip("\n") for x in l.split()] for l in lines]


a = 1
b = 0
p = 0

def execute(ins):
    global a,b,p
    if ins[0] == "hlf":
        if ins[1] == "a":
            a = a/2
        if ins[1] == "b":
            b = b/2
        p +=1

    if ins[0] == "tpl":
        if ins[1] == "a":
            a = a*3
        if ins[1] == "b":
            b = b*3
        p +=1

    if ins[0] == "inc":
        if ins[1] == "a":
            a += 1
        if ins[1] == "b":
            b += 1
        p +=1

    if ins[0] == "jmp":
        p += int(ins[1])

    if ins[0] == "jie":
        if ins[1] == "a":
            if a % 2 == 0:
                p += int(ins[2])
            else:
                p += 1
        if ins[1] == "b":
            if b % 2 == 0:
                p += int(ins[2])
            else:
                p += 1
                
    if ins[0] == "jio":
        if ins[1] == "a":
            if a == 1:
                p += int(ins[2])
            else:
                p += 1
        if ins[1] == "b":
            if b == 1:
                p += int(ins[2])
            else:
                p += 1


while p < len(lines):
    execute(lines[p])
    print(p)
print(b)
