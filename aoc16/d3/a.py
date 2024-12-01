lines = [[int(x)for x in line.split()] for line in open("input.txt","r").readlines()]
tri = 0
for l in lines:
    if ((l[0] + l[1]) > l[2]):
        if ((l[0] + l[2]) > l[1]):
            if ((l[1] + l[2]) > l[0]):
                tri += 1
print(tri)

tri = 0
for idx in range(0,len(lines)-2,3):
    for x in range(3):
        if ((lines[idx][x] + lines[idx+1][x]) > lines[idx+2][x]):
            if ((lines[idx][x] + lines[idx+2][x]) > lines[idx+1][x]):
                if ((lines[idx+2][x] + lines[idx+1][x]) > lines[idx][x]):
                    tri += 1
print(tri)

