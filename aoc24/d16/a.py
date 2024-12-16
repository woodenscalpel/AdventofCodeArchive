f = open("input.txt","r").readlines()

grid = []
startdir = (1,0)

unvisited = {}

for y,line in enumerate(f):
    line = line.strip()
    row = []
    for x,char in enumerate(line):
        if char == "S":
            startpos = (x,y)
            row.append(".")
        elif char == "E":
            endpos = (x,y)
            row.append(".")
        else: row.append(char)
        if char != "#":
            unvisited[((x,y),(1,0))] = [9999999999999999999,[]]
            unvisited[((x,y),(-1,0))] = [9999999999999999999,[]]
            unvisited[((x,y),(0,1))] = [9999999999999999999,[]]
            unvisited[((x,y),(0,-1))] = [9999999999999999999,[]]
    grid.append(row)

unvisited[(startpos,startdir)] = [0,[]]

def gridpos(p):
    return grid[p[1]][p[0]]

def cw(d):
    if d ==(1,0):
        return (0,1)
    if d ==(0,1):
        return (-1,0)
    if d ==(-1,0):
        return (0,-1)
    if d ==(0,-1):
        return (1,0)

def ccw(d):
    if d ==(1,0):
        return (0,-1)
    if d ==(0,-1):
        return (-1,0)
    if d ==(-1,0):
        return (0,1)
    if d ==(0,1):
        return (1,0)

def add(p1,p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def mult(A,p):
    return(p[0]*A,p[1]*A)



print(grid)
print(startpos,endpos)

winningscores = [9999999999999999999999]



def getminscore(elem):
    scores = {}    
    for key, value in elem.items():
        scores[key] = value[0]
    return min(elem,key=elem.get)

winningpaths = []

while unvisited:
    #bestnode = min(unvisited, key=unvisited.get()[1])
    bestnode = getminscore(unvisited)

    pos = bestnode[0]
    direction = bestnode[1]
    score = unvisited[bestnode][0]
    path = unvisited[bestnode][1]
    #forward
    nextpos = add(pos,direction)
    if gridpos(nextpos) != "#":
        if (nextpos,direction) in unvisited:
            if unvisited[(nextpos,direction)][0] > score+1:
                unvisited[(nextpos,direction)] = [score+1,path + [pos]]
            elif unvisited[(nextpos,direction)][0] == score+1:
                unvisited[(nextpos,direction)] = [score+1,list(set(unvisited[(nextpos,direction)][1] +  path + [pos]))]
        if nextpos == endpos:
            winningscores.append(score+1)
            winningpaths.append([score+1,path])

    if (pos,cw(direction)) in unvisited:
        if unvisited[(pos,cw(direction))][0] > score+1000:
            unvisited[(pos,cw(direction))] = [score+1000,path + [pos]]
        elif unvisited[(pos,cw(direction))][0] == score+1000:
            unvisited[(pos,cw(direction))] = [score+1000,list(set(unvisited[(pos,cw(direction))][1] + path + [pos]))]
    if (pos,ccw(direction)) in unvisited:
        if unvisited[(pos,ccw(direction))][0] > score+1000:
            unvisited[(pos,ccw(direction))] = [score+1000,path + [pos]]
        elif unvisited[(pos,ccw(direction))][0] == score+1000:
            unvisited[(pos,ccw(direction))] = [score+1000,list(set(unvisited[(pos,ccw(direction))][1] +  path + [pos]))]
        

    unvisited.pop(bestnode)
    
best = min(winningscores)
print(best)

finalpathset = set()
for path in winningpaths:
    if path[0] == best:
        finalpathset.update(path[1])
print(len(finalpathset)+2)
