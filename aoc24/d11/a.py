from collections import defaultdict
f = open("input.txt","r").read()
stones = [int(x) for x in f.strip().split()]


sdict = defaultdict(int)
for stone in stones:
    sdict[stone] = 1


def memoblink(stones):
    newstones = defaultdict(int)
    for s in stones:
        if s == 0:
            newstones[1] += stones[s]
        elif(len(str(s))%2 == 0):
            newstones[int(str(s)[:int((len(str(s)))/2)])] += stones[s]
            newstones[int(str(s)[int((len(str(s)))/2):])] += stones[s]
        else:
            newstones[s*2024] += stones[s]
    return newstones


for i in range(75):
    newdict = memoblink(sdict)
    sdict = newdict.copy()


gold = 0
for stone in sdict:
    gold += sdict[stone]
print(gold)
