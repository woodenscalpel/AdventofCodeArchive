lines = open("input.txt","r").readlines()

grid = [[False for x in range(50)]for y in range(6)]

print(lines)

def rect(g,x,y):
    for i in range(y):
        for j in range(x):
            g[i][j] = True
    return g

def rrotate(grid,num1,num2):
    grid[num1] = grid[num1][-(num2):] + grid[num1][:-(num2)]
    print(len(grid[num1]))
    return grid

def crotate(grid,num1,num2):
    col = [grid[r][num1] for r in range(6)]
    #col = col[num2+1:] + col[:num2+1]
    col = col[-num2:] + col[:-num2]
    for y in range(6):
        grid[y][num1] = col[y]
    print("c",len(grid))
    return grid
    #grid[num1] = [grid[num1][num2:]] + grid[num1][:num2]
    #return grid


"""
grid = [[False for x in range(9)]for y in range(6)]
grid = rect(grid,3,2)
print(grid)
grid = crotate(grid,1,1)
print(grid)
grid = rrotate(grid,0,4)
print(grid)
input()
"""

for line in lines:
    line = line.strip().split()
    #print(line)
    if(line[0] == "rect"):
        coords = line[1].split("x")
        #print(grid)
        grid = rect(grid,int(coords[0]),int(coords[1]))
    else:
        num1 = int(line[2][2:])
        num2 = int(line[4])
        if(line[1] == "row"):
            grid = rrotate(grid,num1,num2)
        if(line[1] == "column"):
            grid = crotate(grid,num1,num2)
    #print(grid)
total = 0
for x in grid:
    for y in x:
        if y:
            total +=1
print(total)
for c in grid:
    for x in c:
        if x:
            print("#",end='')
        else:
            print(".",end='')
    print("\n")
    #print(c)
