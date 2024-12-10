f = open("input.txt","r").readlines()

grid = [[int(x) for x in line.strip()] for line in f]
maxx = len(grid[0])
maxy = len(grid)

def getn(pos):
    x = pos[0]
    y = pos[1]
    neigh = []
    if x-1 > -1:   neigh.append((x-1,y))
    if y-1 > -1:   neigh.append((x,y-1))
    if x+1 < maxx: neigh.append((x+1,y))
    if y+1 < maxy: neigh.append((x,y+1))
    return(neigh)

def gridpos(pos):
    return grid[pos[0]][pos[1]]

def walk(posl,h):
    if h ==9:
        return posl
    newposl = []   # = set() for p1
    for pos in posl:
        neigh = getn(pos)
        for n in neigh:
            if gridpos(n) == h+1:
                newposl.append(n) # .add(n) for part 1
    return walk(newposl,h+1)

silver = 0
gold  = 0
for i in range(maxx):
    for j in range(maxy):
        if grid[i][j] == 0:
            silver += len(set(walk([(i,j)],0)))
            gold += len(walk([(i,j)],0))
print(silver, gold)
