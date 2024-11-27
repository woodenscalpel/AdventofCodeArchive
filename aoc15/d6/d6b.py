lines = open("input.txt","r").read().split("\n")
#lines = ["turn off 0,0 th 2,2,"]

grid = [[0 for x in range(1001)] for y in range(1001)]

for line in lines:
    line = line.split()
    if line:
        if(line[0] == "toggle"):
            start = line[1].split(",")
            end = line[3].split(",")
            for i in range(int(start[0]),int(end[0])+1):
                for j in range(int(start[1]),int(end[1])+1):
                    grid[i][j] += 2

        if(line[0] == "turn"):
            start = line[2].split(",")
            end = line[4].split(",")

            for i in range(int(start[0]),int(end[0])+1):
                for j in range(int(start[1]),int(end[1])+1):
                    if line[1] == "on":
                        grid[i][j] += 1
                    if line[1] == "off":
                        grid[i][j] -= 1
                        if grid[i][j] < 0: grid[i][j] = 0
                    

count = 0
for i in range(1001):
    for j in range(1001):
        count += grid[i][j]
print(count)


