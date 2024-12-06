f = open("input.txt","r").readlines()

area = {}
for r,line in enumerate(f):
    line = line.strip()
    row = {}
    area[r] = {}
    for c,x in enumerate(line): 
        if x == "^":
            startpos = (r,c)
            area[r][c] = "X"
        else:
            area[r][c] = x
print(area)
print(startpos)
maxlen = len(area)
startdir = (-1,0)

def add(t1,t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def rotate(d):
    if d == (0,-1):
        return (-1,0)
    if d == (1,0):
        return (0,-1)
    if d == (0,1):
        return (1,0)
    if d == (-1,0):
        return (0,1)

def move(p,d):
    np = add(p,d)
    if np[0] > maxlen-1 or np[1] > maxlen-1 or np[0] == -1 or np[-1] == -1:
        print("DONE")
        print(area)
        silver = 1
        for row in area:
            for c in area[row]:
                if area[row][c] == "X":
                    silver += 1
        print(silver)
        input()
    if area[np[0]][np[1]] == "#":
        d = rotate(d)
    else:
        area[p[0]][p[1]] = "X"
        p = np
    return p,d

p,d = move(startpos,startdir)
print(maxlen)
input()
while True:
    p,d = move(p,d)
    #print(area)
    print(p,d)
    #input()
