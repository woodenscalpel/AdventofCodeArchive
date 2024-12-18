f = open("input.txt","r").readlines()

gridsize = 71
inp = []
for line in f:
    line = line.strip().split(",")
    inp.append((int(line[0]),int(line[1])))


def genunvisited():
    unvisited = {}
    for x in range(gridsize):
        for y in range(gridsize):
            unvisited[(x,y)] = 999999999999999999

    unvisited[(0,0)] = 0
    return unvisited



def getn(pos):
    x = pos[0]
    y = pos[1]
    neigh = []
    if x-1 > -1:   neigh.append((x-1,y))
    if y-1 > -1:   neigh.append((x,y-1))
    if x+1 < gridsize: neigh.append((x+1,y))
    if y+1 < gridsize: neigh.append((x,y+1))
    return(neigh)


def getmin(u):
    return min(u,key=u.get)


#print(inp)
#print(inp[:12])
visited = {}
numfallen = 2900

good = True
while good:
    print(numfallen)
    unvisited = genunvisited()
    visited = {}
    numfallen+=1

    fallen = inp[:numfallen]
    while unvisited:
        bestnode = getmin(unvisited)
        for n in getn(bestnode):
            if n not in fallen:
                if n in unvisited:
                    if unvisited[n] > unvisited[bestnode]+1:
                        unvisited[n] = unvisited[bestnode]+1
        visited[bestnode] = unvisited[bestnode]
        unvisited.pop(bestnode)
    #print(visited[(gridsize-1,gridsize-1)])
    if visited[(gridsize-1,gridsize-1)] > 9999999999:
        good = False

print(numfallen)
print(inp[numfallen-1])
