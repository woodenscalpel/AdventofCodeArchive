f = open("input.txt","r").read().strip()

halves = f.split("\n\n")


rules = {}

for line in halves[0].split("\n"):
    line = line.split("|")
    if int(line[0]) not in rules:
        rules[int(line[0])] = []
    rules[int(line[0])].append(int(line[1]))


goodlines = []
badlines = []

for line in halves[1].split("\n"):
    line = [int(x) for x in line.split(",")]
    linel = len(line)
    goodline = True
    for idx,num in enumerate(line):
        for b in range(idx):
            #before
            #if number before is stated to be after thats bad
            if num in rules:
                if line[b] in rules[num]:
                    goodline = False
        for a in range(idx,linel-1):
            #after
            #if a number after has a rule for this number to be before thats bad
            if line[a] in rules:
                if num in rules[line[a]]:
                    goodline = False
    if goodline:
        goodlines.append(line)
    else:
        badlines.append(line)

ans = 0
for line in goodlines:
    ans += line[int(len(line)/2)]
print(ans)

def goodlinecheck(line):
    linel = len(line)
    goodline = True
    for idx,num in enumerate(line):
        for b in range(idx):
            #before
            #if number before is stated to be after thats bad
            if num in rules:
                if line[b] in rules[num]:
                    goodline = False
        for a in range(idx,linel-1):
            #after
            #if a number after has a rule for this number to be before thats bad
            if line[a] in rules:
                if num in rules[line[a]]:
                    goodline = False
    return goodline


def mutateline(line):
    linel = len(line)
    for idx,num in enumerate(line):
            for b in range(idx):
                #before
                #if number before is stated to be after thats bad
                if num in rules:
                    if line[b] in rules[num]:
                        newlist = line[0:idx+1]
                        newlist2 = line[idx+1:]
                        #print(line,newlist,newlist2)
                        newlist.remove(line[b])
                        return newlist + [line[b]] + newlist2
                        goodline = False
            for a in range(idx,linel-1):
                #after
                #if a number after has a rule for this number to be before thats bad
                if line[a] in rules:
                    if num in rules[line[a]]:
                        goodline = False
                        newlist = line[0:idx]
                        newlist3 = line[idx:a]
                        newlist2 = line[a+1:]
                        return newlist + [line[a]] + newlist3 + newlist2





fixedlines = []
for line in badlines:
    goodline = False
    while not goodline:
        line = mutateline(line)
        goodline = goodlinecheck(line)
    fixedlines.append(line)

ans = 0
for line in fixedlines:
    ans += line[int(len(line)/2)]
print(ans)
