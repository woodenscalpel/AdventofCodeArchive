lines = open("input.txt","r").readlines()

leftlist = []
rightlist = []

for line in lines:
    line = line.strip()
    line = line.split()
    leftlist.append(int(line[0]))
    rightlist.append(int(line[1]))

leftlist = sorted(leftlist)
rightlist = sorted(rightlist)
totaldiff = 0
for x in range(len(leftlist)):
    diff = abs(rightlist[x] - leftlist[x])
    totaldiff += diff

print(totaldiff)

p2 = 0
for x in leftlist:
    n = 0
    for y in rightlist:
        if y == x:
            n += 1
    p2 += x*n
print(p2)
