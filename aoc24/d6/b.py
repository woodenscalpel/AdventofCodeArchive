from copy import deepcopy
f = open("test.txt","r").readlines()

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

def move(p,d,grid):
    np = add(p,d)
    if np[0] > maxlen-1 or np[1] > maxlen-1 or np[0] == -1 or np[-1] == -1:
        #print("DONE")
        silver = 1
        for row in grid:
            for c in grid[row]:
                if grid[row][c] == "X":
                    silver += 1
        #print(silver)
        return -999,-999
    if grid[np[0]][np[1]] == "#":
        d = rotate(d)
    else:
        grid[p[0]][p[1]] = "X"
        p = np
    return p,d

p,d = move(startpos,startdir,area)
#print(maxlen)
while True:
    p,d = move(p,d,area)
    #print(area)
    #print(p,d)
    if p == -999:
        break
    #input()

gold = 0
good = []
print(startpos)
for x in range(maxlen):
    for y in range(maxlen):
        newgrid = deepcopy(area)
        newgrid[x][y] = "#"
        #print(newgrid)
        
        p,d = move(startpos,startdir,newgrid)
        for i in range(2000):
            p,d = move(p,d,newgrid)
            #print(area)
            if p == -999:
                break

        if p != -999:
            gold+=1
            good.append((x,y))
print(gold,good)


