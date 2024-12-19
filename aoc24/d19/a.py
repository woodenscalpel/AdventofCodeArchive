f = open("input.txt","r").read().strip()

f = f.split("\n\n")

patterns = [x.lstrip() for x in f[0].split(",")]
designs = [x.lstrip() for x in f[1].split("\n")]


print(patterns,designs)

def matchpattern(statesandcompletion):
    
    states = statesandcompletion[0]
    completionnum = statesandcompletion[1]
    newstates = {}
    for statelist in states:
        state = statelist[0]
        num = statelist[1]
        for p in patterns:
            if p == state[:len(p)]:
                if len(state) > len(p):
                    if state[len(p):] in newstates:
                        newstates[state[len(p):]] += num
                    else:
                        newstates[state[len(p):]] = num
                if state == p:
                    completionnum += num
    returnstates = []
    for s in newstates:
        returnstates.append([s,newstates[s]])
    return [returnstates,completionnum]


silver = 0
gold = 0
for d in designs:
    found = True
    remaining = [[[d,1]],0]
    
    while remaining[0] != []:
        remaining = matchpattern(remaining)
    if remaining[1] > 0 : silver += 1
    gold += remaining[1]
print(silver)
print(gold)

