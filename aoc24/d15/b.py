f = open("input.txt","r").read()

f = f.split("\n\n")

rawgrid = f[0]
moves = f[1]
grid = []
for row in rawgrid.split("\n"):
    line = ""
    for x in row:
        if x == "#":
            line += "##"
        if x == ".":
            line += ".."
        if x == "@":
            line += "@."
        if x == "O":
            line += "[]"
    grid.append([i for i in line])

h = len(grid)
w = len(grid[0])

def printgrid(pos):
    for idx,row in enumerate(grid):
        for idx2,char in enumerate(row):
            if (idx2,idx) == pos:
                print("@",end="")
            else:
                print(char,end="")
        print("")



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


def testhmove(p,d,dist):
    checkpos = add(p, mult(dist,d))
    symbol = getpos(checkpos)
    if symbol == ".":
        return True
    if symbol == "#":
        return False
    if symbol == "[" or symbol == "]":
        return testhmove(p,d,dist+1)

def testvmove(p,d,dist):
    checkpos = add(p, mult(dist,d))
    symbol = getpos(checkpos)
    if symbol == ".":
        return True
    if symbol == "#":
        return False
    if symbol == "[":
        return (testvmove(p,d,dist+1) and testvmove(add(p,(1,0)),d,dist+1))
    if symbol == "]":
        return (testvmove(p,d,dist+1) and testvmove(add(p,(-1,0)),d,dist+1))

def executevmove(p,d,dist):
    checkpos = add(p, mult(dist,d))
    symbol = getpos(checkpos)
    #print("executing",checkpos)
    if symbol == ".":
        #oldpos = add(p, mult(dist-1,d))
        #grid[checkpos[1]][checkpos[0]] = getpos(oldpos)
        #return [checkpos]
        return []
    if symbol == "#":
        return False
    if symbol == "[":
        leftpos = p
        rightpos = add((1,0),leftpos)
    if symbol == "]":
        rightpos = p
        leftpos = add((-1,0),rightpos)
    #print(leftpos,rightpos)
    leftcheckpos = add(leftpos, mult(dist,d))
    rightcheckpos = add(rightpos, mult(dist,d))
    return [leftcheckpos] + executevmove(rightpos,d,dist+1) + executevmove(leftpos,d,dist+1)
    #return executevmove(rightpos,d,dist+1) + executevmove(leftpos,d,dist+1)

    """
    oldleftpos = add(leftpos, mult(dist-1,d))
    leftcheckpos = add(leftpos, mult(dist,d))
    oldrightpos = add(rightpos, mult(dist-1,d))
    rightcheckpos = add(rightpos, mult(dist,d))
    print(leftpos,oldleftpos)
    grid[leftcheckpos[1]][leftcheckpos[0]] = getpos(oldleftpos)
    grid[rightcheckpos[1]][rightcheckpos[0]] = getpos(oldrightpos)
    """





    
def executehmove(p,d,dist):
    checkpos = add(p, mult(dist,d))
    symbol = getpos(checkpos)
    if symbol == ".":
        oldpos = add(p, mult(dist-1,d))
        grid[checkpos[1]][checkpos[0]] = getpos(oldpos)
        return True
    if symbol == "#":
        return False
    if symbol == "[" or "]":
        executehmove(p,d,dist+1)
        oldpos = add(p, mult(dist-1,d))
        grid[checkpos[1]][checkpos[0]] = getpos(oldpos)


def testmove(p,d,dist):
    if d[0] != 0:
        return testhmove(p,d,dist)
    else:
        return testvmove(p,d,dist)

def executechanges(updates,direction):

    if direction[1] == 1:
        updates = reversed(sorted(updates,key= lambda x: x[1]))
    else:
        updates = sorted(updates,key= lambda x: x[1])
    
    for update in updates:
        new = add(update,direction)
        grid[new[1]][new[0]] = grid[update[1]][update[0]]
        grid[new[1]][new[0]+1] = grid[update[1]][update[0]+1]
        grid[update[1]][update[0]+1] = "."
        grid[update[1]][update[0]] = "."

def executemove(p,d,dist):
    if d[0] != 0:
        return executehmove(p,d,dist)
    else:
        updatelist = executevmove(p,d,dist)
        print(updatelist)
        updatelist = list(dict.fromkeys(updatelist))
        executechanges(updatelist,d)

        return True

def domove(p,d):
    test = testmove(p,d,1)
    print(test)
    if test:
        executemove(p,d,1)
        return add(p,d)
    return p

pos = startpos
for m in moves:
    print(m)
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
    print(pos)
    #printgrid(pos)
    #input()

silver = 0
for y in range(h):
    for x in range(w):
        if getpos((x,y)) == "[":
            silver += 100*y+x

print(silver)

