lines = open("input.txt","r").read().split("\n")
#lines = ["turn off 0,0 th 2,2,"]

grid = [[False for x in range(1001)] for y in range(1001)]

for line in lines:
    line = line.split()
    if line:
        if(line[0] == "toggle"):
            start = line[1].split(",")
            end = line[3].split(",")
            c = 0
            for i in range(int(start[0]),int(end[0])+1):
                for j in range(int(start[1]),int(end[1])+1):
                    grid[i][j] = not grid[i][j]
                    c = c+1
            print(c)

        if(line[0] == "turn"):
            start = line[2].split(",")
            end = line[4].split(",")
            print(start)
            print(end)
            print(line[1])
            c = 0

            for i in range(int(start[0]),int(end[0])+1):
                for j in range(int(start[1]),int(end[1])+1):
                    if line[1] == "on":
                        grid[i][j] = True
                    if line[1] == "off":
                        grid[i][j] = False
                    
                    c = c+1
            print(c)

count = 0
for i in range(1001):
    for j in range(1001):
        if grid[i][j] == True:
            count += 1
print(count)


