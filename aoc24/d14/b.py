f = open("input.txt","r").readlines()

#maxx = 11
#maxy = 7

maxx = 101
maxy = 103

robots = []

for line in f:
    line = line.split()
    p = [int(x) for x in line[0].split("=")[1].split(",")]
    v = [int(x) for x in line[1].split("=")[1].split(",")]
    robots.append([p,v])


def display(robots,n):
    for y in range(maxy):
        for x in range(maxx):
            on = False
            for r in robots:
                pos = r[0]
                if pos[0] == x and pos[1] == y:
                    on = True
            if on:
                print("#",end='')
            else:
                print(".",end='')
        print("")
    print(n, "***********************************")


def timestep(robots,i):
    nextrobots = []
    for r in robots:
        #print(r)
        pos = r[0]
        vel = r[1]
        newpos = [[(pos[0] + vel[0]) % maxx, (pos[1] + vel[1]) % maxy],vel]
        nextrobots.append(newpos)
    if i > 1000:
        display(robots,i)
    return nextrobots

for i in range(10000):
    robots = timestep(robots,i)
#print(robots)


q1=0
q2=0
q3=0
q4=0
for r in robots:
    pos = r[0]
    if pos[0] < (maxx-1)/2 and pos[1] < (maxy-1)/2: q1 += 1
    if pos[0] < (maxx-1)/2 and pos[1] > (maxy-1)/2: q2 += 1
    if pos[0] > (maxx-1)/2 and pos[1] < (maxy-1)/2: q3 += 1
    if pos[0] > (maxx-1)/2 and pos[1] > (maxy-1)/2: q4 += 1
silver = q1*q2*q3*q4
print(silver)
