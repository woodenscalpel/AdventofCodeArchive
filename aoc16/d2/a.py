instructions = open("input.txt","r").readlines()
ins = [x.strip() for x in instructions]


pos = [0,0] #x,y

for i in ins:
    for c in i:
        if c == "L":
            pos[0] = max(-1, pos[0]-1)
        if c == "D":
            pos[1] = max(-1, pos[1]-1)
        if c == "U":
            pos[1] = min(1, pos[1]+1)
        if c == "R":
            pos[0] = min(1, pos[0]+1)
    print(pos)
