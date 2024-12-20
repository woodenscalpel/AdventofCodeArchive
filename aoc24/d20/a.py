f = open("input.txt","r").readlines()


walls = []
unvisited = {}

ysize = len(f)
xsize = len(f[0].strip())

for y,line in enumerate(f):
    line = line.strip()
    #row = []
    for x,char in enumerate(line):
        if char == "S":
            startpos = (x,y)
            #row.append(".")
        elif char == "E":
            endpos = (x,y)
            #row.append(".")
        #else: row.append(char)
        if char != "#":
            unvisited[(x,y)] = 9999999999999999999
        if char == "#":
            walls.append((x,y))
    #grid.append(row)


unvisited[startpos] = 0



def getn(pos):
    x = pos[0]
    y = pos[1]
    neigh = []
    if x-1 > -1:   neigh.append((x-1,y))
    if y-1 > -1:   neigh.append((x,y-1))
    if x+1 < xsize: neigh.append((x+1,y))
    if y+1 < ysize: neigh.append((x,y+1))
    return(neigh)


def getmin(u):
    return min(u,key=u.get)


visited = {}

cheat = False

while unvisited:
    bestnode = getmin(unvisited)
    for n in getn(bestnode):
        if n not in walls:
            if n in unvisited:
                if unvisited[n] > unvisited[bestnode]+1:
                    unvisited[n] = unvisited[bestnode]+1
    visited[bestnode] = unvisited[bestnode]
    unvisited.pop(bestnode)

shortcuts = []
shorttime = 20
for item in visited:
    pos = [item]
    phasepos = []
    for x in visited:
        mandist = abs(item[0] - x[0]) + abs(item[1]-x[1])
        if  mandist <= shorttime:
            phasepos.append([x,mandist])

    startdistance = visited[item]
    for p in phasepos:
        if p[0] in visited:
            enddistance = visited[p[0]]
            shortcuts.append(enddistance-startdistance - p[1])
gold = 0
for s in shortcuts:
    if s > 99:
        gold +=1
print(gold)


