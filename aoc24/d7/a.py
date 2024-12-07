f = open("input.txt","r").readlines()


def doop(numlist):
    if isinstance(numlist,int):
        return [numlist]
    if len(numlist) == 1:
        return numlist
    return [ numlist[0] + x for x in  doop(numlist[1:])] + [numlist[0]*x for x in doop(numlist[1:])]

def concat(a,b):
    return int(str(b) + str(a))

def doop2(numlist):
    if isinstance(numlist,int):
        return [numlist]
    if len(numlist) == 1:
        return numlist
    return [ numlist[0] + x for x in  doop2(numlist[1:])] + [numlist[0]*x for x in doop2(numlist[1:])] + [concat(numlist[0],x) for x in doop2(numlist[1:])]


silver = 0
for line in f:
    line = line.strip().split()
    goal = int(line[0][:-1])
    nums = list(reversed([int(x) for x in line[1:]]))
    results = doop(nums)
    #print(goal,results)
    found = False
    for r in results:
        if r == goal:
            #print("!")
            found = True
    if found: silver += goal

print("s",silver)
gold = 0
for line in f:
    line = line.strip().split()
    goal = int(line[0][:-1])
    nums = list(reversed([int(x) for x in line[1:]]))
    results = doop2(nums)
    #print(goal,results)
    found = False
    for r in results:
        if r == goal:
            #print("!")
            found = True
    if found: gold += goal
print("g",gold)
