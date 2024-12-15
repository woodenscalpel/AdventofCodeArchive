f = open("input.txt","r").read()

f = f.split("\n\n")

rawgrid = f[0]
moves = f[1]
grid = []
for row in rawgrid.split("\n"):
    grid.append([x for x in row])

h = len(grid)
w = len(grid[0])

def getpos(pos):
    return grid[pos[1]][pos[0]]

for y in range(h):
    for x in range(w):
        if getpos((x,y)) == "@":
            startpos = (x,y)
            grid[y][x] = "."

def add(p1,p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def mult(A,p):
    return(p[0]*A,p[1]*A)

def scan(pos,direction,checkdist):
    #scan until free space or wall. returns delta of space or wall. box recursively adds 1 to dist and checkpos
    checkpos = add(pos, mult(checkdist,direction))
    symbol = getpos(checkpos)
    if symbol == ".":
        return checkdist
    if symbol == "#":
        return -1
    if symbol == "O":
        return scan(pos,direction,checkdist+1)

def domove(p,d):
    distance = scan(p,d,1)
    if distance == -1:
        return p
    else:
        newpos = add(p,d)
        grid[newpos[1]][newpos[0]] = "."
        for i in range(1,distance):
            boxpos = add(p,mult(distance,d))
            grid[boxpos[1]][boxpos[0]] = "O"
        return newpos


pos = startpos
for m in moves:
    #print(m)
    if m == "\n":
        pass
    if m == "^":
        pos = domove(pos,(0,-1))
    if m == ">":
        pos = domove(pos,(1,0))
    if m == "<":
        pos = domove(pos,(-1,0))
    if m == "v":
        pos = domove(pos,(0,1))
    #print(pos)

for row in grid:
    for char in row:
        print(char,end="")
    print("")

silver = 0
for y in range(h):
    for x in range(w):
        if getpos((x,y)) == "O":
            silver += 100*y+x

print(silver)

