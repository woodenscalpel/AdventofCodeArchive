from copy import deepcopy
from collections import defaultdict
import itertools
"""
initialfloors = [set([("M","H"),("M","L")]),
                 set([("G","H")]),
                 set([("G","L")]),
                 set(),
                 0] #Elevator pos
#Part 1
initialfloors = [set([("G","P"),("M","P")]),
                 set([("G","Co"),("G","Cu"),("G","R"),("G","Pl")]),
                 set([("M","Co"),("M","Cu"),("M","R"),("M","Pl")]),
                 set(),
                 0] #Elevator pos

"""

initialfloors = [set([("G","P"),("M","P"),("G","El"),("M","El"),("G","D"),("M","D")]),
                 set([("G","Co"),("G","Cu"),("G","R"),("G","Pl")]),
                 set([("M","Co"),("M","Cu"),("M","R"),("M","Pl")]),
                 set(),
                 0] #Elevator pos
states = [initialfloors]
turncount = 0

def getpermutations(l):
    perms = []
    for first in range(len(l)):
        for second in range(-1,len(l)): #-1 to allow only 1
            if first != second:
                if second == -1:
                    perms.append([l[first]])
                else:
                    perms.append([l[first],l[second]])
    return perms

def moveupstates(state):
    newstates = []

    elevator = state[4]
    oldfloor = state[elevator]
    if len(oldfloor) < 1:
        return []
    if elevator < 3:
        permutationlist = []
        for perm in itertools.permutations(oldfloor,1):
            permutationlist.append(perm)
        for perm in itertools.permutations(oldfloor,2):
            permutationlist.append(perm)
        for permutations in permutationlist:
            oldfloor = state[elevator].copy()
            newfloor = state[elevator+1].copy()
            for p in permutations:
                oldfloor.remove(p)
                newfloor.add(p)
            oldexplode = explodecheck(oldfloor)
            newexplode = explodecheck(newfloor)
            if oldexplode or newexplode:
                continue
            newstate = state.copy()
            newstate[elevator] = oldfloor
            newstate[elevator+1] = newfloor
            newstate[4] +=1
            newstates.append(newstate)
            if newstate[0] == set() and newstate[1] == set() and newstate[2] == set():
                print("DONE",newstate)
                input()
        return newstates
    else:
        return []

def movedownstates(state):
    newstates = []
    elevator = state[4]
    oldfloor = state[elevator]
    if len(oldfloor) < 1:
        return []
    if elevator > 0:
        permutationlist = []
        for perm in itertools.permutations(oldfloor,1):
            permutationlist.append(perm)
        for perm in itertools.permutations(oldfloor,2):
            permutationlist.append(perm)
        for permutations in permutationlist:
            """
            if elevator == 3 and len(permutations) == 2:
                continue
                """
            oldfloor = state[elevator].copy()
            newfloor = state[elevator-1].copy()
            for p in permutations:
                oldfloor.remove(p)
                newfloor.add(p)
            oldexplode = explodecheck(oldfloor)
            newexplode = explodecheck(newfloor)
            if oldexplode or newexplode:
                continue
            newstate = state.copy()
            newstate[elevator] = oldfloor
            newstate[elevator-1] = newfloor
            newstate[4] -=1
            newstates.append(newstate)
        return newstates

    else:
        return []

def prune(states):
    prunedstates = []
    for state in states:
        hashes = []
        for item in [("G","P"),("M","P"),("G","El"),("M","El"),("G","D"),("M","D"),("G","Co"),("G","Cu"),("G","R"),("G","Pl"),("M","Co"),("M","Cu"),("M","R"),("M","Pl")]:
            for x in range(4):
                if item in state[x]:
                    hashes.append(x)
                    break
        #lenhash = (len(state[0]),len(state[1]),len(state[2]),len(state[3]),extrahash,extrahash2,extrahash3,extrahash4)
        lenhash = tuple(hashes)

        dupe = False
        for p in seenstates[lenhash]:
            if p[0] == state[0]:
                if p[1] == state[1]:
                    if (p[2]) == state[2]:
                        if (p[3]) == (state[3]):
                            if p[4] == state[4]:
                                dupe = True
                                break
        if dupe == False:
            prunedstates.append(state)
            seenstates[lenhash].append(state)
    return prunedstates

def explodecheck(floor):
    explode = False
    safe = False
    for item in floor:
        explode = False
        safe = False
        if item[0] == "M":
            for item2 in floor:
                if item2[0] == "G":
                    if item[1] == item2[1]:
                        safe = True
                    if item[1] != item2[1]:
                        explode = True
        if explode and not safe:
            break
    if safe or not explode:
        return False
    return True



print(initialfloors)
turns = 1

seenstates = defaultdict(list)

while states:
    turns += 1
    newstates = []
    for state in states:
        newstates += moveupstates(state)
        newstates += movedownstates(state)
    #print(newstates)
    states = prune(newstates)
    print(len(states))
    print("T:", turns)
    """
    for s in states:
        print("S")
        for f in s:
            print(f)
        input()

"""
