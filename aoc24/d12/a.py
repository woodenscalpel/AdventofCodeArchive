f = open("input.txt","r").readlines()


def getn(pos):
    x = pos[0]
    y = pos[1]
    neigh = []
    if x-1 > -1:   neigh.append((x-1,y))
    if y-1 > -1:   neigh.append((x,y-1))
    if x+1 < maxx: neigh.append((x+1,y))
    if y+1 < maxy: neigh.append((x,y+1))
    return(neigh)

def getngold(pos):
    x = pos[0]
    y = pos[1]
    neigh = []
    neigh.append((x-1,y))
    neigh.append((x,y-1))
    neigh.append((x+1,y))
    neigh.append((x,y+1))
    return(neigh)



def gridpos(pos):
    return grid[pos[0]][pos[1]][0]
def inregion(pos):
    return grid[pos[0]][pos[1]][1]


def populatereigons():
    #regions are a list of points. can get perimeter thru neighbour analysis
    regions = []
    for i in range(maxx):
        for j in range(maxy):
            if not inregion((i,j)):
                regions.append(floodfill((i,j)))
    return regions


def floodfill(startpos):
    stack = [startpos]
    reigonmembers = [startpos]
    symbol = gridpos(startpos)
    grid[startpos[0]][startpos[1]][1] = True
    while stack:
        pos = stack.pop()
        neighbours = getn(pos)
        for n in neighbours:
            s = gridpos(n)
            if s == symbol:
                if n not in reigonmembers:
                    stack.append(n)
                    reigonmembers.append(n)
                    grid[n[0]][n[1]][1] = True
    return reigonmembers

def area(r):
    return len(r)
def perim(r):
    p = 0
    symbol = gridpos(r[0])
    for item in r:
        neighbours = getn(item)
        p += 4 - len(neighbours)
        for n in neighbours:
            if gridpos(n) != symbol:
                p += 1
    return p

def add(p1,p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def ridx(i):
    return (i+1) %4
def lidx(i):
    if i-1<0:
        return 3
    return i-1

def inbounds(pos):
    return -1 < pos[0] and pos[0] < maxx and -1 < pos[1] and pos[1] < maxy

def gridpos2(pos):
    if not inbounds(pos):
        return "I HATE EDGE CASES I HATE EDGE CASES AAAAAAAAA"
    return grid[pos[0]][pos[1]][0]

def goldperim(reigon):
    #start at point where +y neighbour is not part of reigon.
    #start building wall to the right. 'turn' wall when encounter corner and add to wall count
    wallnum = 0
    symbol = gridpos(reigon[0])
    for r in reigon:
        if gridpos2((r[0],r[1]+1)) != symbol:
            startr = r
            break

    dirs = [(0,1),(1,0),(0,-1),(-1,0)] #increase index to rotate right, decrease for left
    checkdir = 0 #start checking north
    movedir = 1 #start moving right

    r = startr
    #input()
    initmove = False
    loop = True
    while loop:
        if r== startr and checkdir == 0 and initmove == True:
            loop = False
            break
        if r == startr and wallnum == 4 and initmove == False:
            break

        checkpos = add(r,dirs[checkdir])
        movepos = add(r,dirs[movedir])
        print("current", r)
        print("s", symbol)
        print("checkpos",checkpos)
        print("movepos",movepos)
        print("walls", wallnum)
        input()

        if gridpos2(checkpos) != symbol:
            if gridpos2(movepos) == symbol:
                #print("choseA")
                r = movepos
                initmove = True
            else:
                #print("choseB")
                checkdir = ridx(checkdir)
                movedir = ridx(movedir)
                wallnum += 1
        else:
            #print("choseC")
            r = checkpos
            initmove = True
            movedir = checkdir
            checkdir = lidx(checkdir)
            wallnum += 1
    return wallnum


def goldperim2(reg):
    edges = []
    symbol = gridpos(reg[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)] 
    walls = 0

    for r in reg:
        for d in dirs:
            n = add(r,d)
            if gridpos2(n) != symbol:
                edges.append([r,d])
    while edges:
        edges = removeconnectededges(edges)
        walls+=1
    return walls


def removeconnectededges(edges):
    compare = edges.pop()
    stack = [compare]
    while stack:
        compare = stack.pop()
        d = compare[1]
        neighs = getngold(compare[0])
        newedges = []
        for e in edges:
            match = False
            for n in neighs:
                if e[0] == n and e[1] == d:
                    stack.append(e)
                    match = True
            if match == False:
                newedges.append(e)
        edges = newedges
    return edges



grid = [[[x,False] for x in line.strip()] for line in f]
maxx = len(grid[0])
maxy = len(grid)

reigons = populatereigons()
silver = 0
gold = 0
for r in reigons:
    silver += area(r)*perim(r)
    gold += area(r)*goldperim2(r)
print(silver)
print(gold)
