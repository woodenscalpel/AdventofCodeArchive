
grid = {}
for i,line in enumerate(open("input.txt","r").readlines()):
    grid[i] = {}
    for j,char in enumerate(line):
        if char == "#":
            grid[i][j] = True


#print(grid)


def neighbourcount(grid,i,j):
    n=0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if not(x == i and y == j):
                if x in grid:
                    if y in grid[x]:
                        if(grid[x][y]):
                            n += 1
    return n 

def timestep(grid):
    newgrid = {}
    for i in range(100):
        newgrid[i] = {}
        for j in range(100):
            ncount = neighbourcount(grid,i,j)
            #print(i,j,ncount)
            if i in grid:
                if j in grid[i]:
                    if grid[i][j]:
                        if ncount == 2 or ncount == 3:
                            newgrid[i][j] = True
                if ncount == 3: 
                    newgrid[i][j] = True
    newgrid[0][0] = True
    newgrid[0][99] = True
    newgrid[99][99] = True
    newgrid[99][0] = True
    return newgrid
                

steps = 100
for s in range(steps):
    grid = timestep(grid)


final = 0
for i in range(100):
    for j in range(100):
        if i in grid:
            if j in grid[i]:
                
                if grid[i][j]:
                    final += 1

print(final)
