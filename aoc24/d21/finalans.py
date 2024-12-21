from collections import defaultdict
import random
codes = open("input.txt","r").readlines()

firstkeypad = [["X","0","A"],
               ["1","2","3"],
               ["4","5","6"],
               ["7","8","9"]]

dirkeypad = [["<","v",">"],
             ["X","^","A"]]



def getcodepos(target,keypad):
    for y in range(len(keypad)):
        for x in range(len(keypad[0])):
            if keypad[y][x] == target:
                return (x,y)

def getxdir(p,t):
    if p[0] == t[0]:
        return 0
    if p[0] > t[0]:
        return -1
    if p[0] < t[0]:
        return 1

def getydir(p,t):
    if p[1] == t[1]:
        return 0
    if p[1] > t[1]:
        return -1
    if p[1] < t[1]:
        return 1

def mandist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def path1better(p1,p2):
    if p1[-1] == "^" or p1[-1] == ">":
        return True
    return False


def genkeypadinputs(code,keypad,startkey = "A"):
    position = getcodepos(startkey,keypad)
    possibleinstructions = [""]
    for digit in code:
        targetpos = getcodepos(digit,keypad)
        xdir = getxdir(position,targetpos)
        ydir = getydir(position,targetpos)
        xdist = abs(position[0] - targetpos[0])
        ydist = abs(position[1] - targetpos[1])

        #generate both paths to get to button. discard paths that go through X. take first one that doesnt
    #x first
        path1 = ["",[]]
        testpos = position
        if targetpos == position:
            newins = []
            for i in possibleinstructions:
                newins.append(i + "A")
            possibleinstructions = newins
            continue
        for i in range(xdist):
            testpos = (testpos[0]+xdir,testpos[1]) 
            path1[1].append(testpos)
            if xdir == 1: path1[0] += ">"
            if xdir == -1: path1[0] += "<"
        for i in range(ydist):
            testpos = (testpos[0],testpos[1]+ydir) 
            path1[1].append(testpos)
            if ydir == 1: path1[0] += "^"
            if ydir == -1: path1[0] += "v"
        path2 = ["",[]]
        testpos = position
        for i in range(ydist):
            testpos = (testpos[0],testpos[1]+ydir) 
            path2[1].append(testpos)
            if ydir == 1: path2[0] += "^"
            if ydir == -1: path2[0] += "v"
        for i in range(xdist):
            testpos = (testpos[0]+xdir,testpos[1]) 
            path2[1].append(testpos)
            if xdir == 1: path2[0] += ">"
            if xdir == -1: path2[0] += "<"
        path1good = True
        for item in path1[1]:
            if keypad[item[1]][item[0]] == "X": path1good = False
        path2good = True
        for item in path2[1]:
            if keypad[item[1]][item[0]] == "X": path2good = False
        #if mandist(getcodepos(path1[0][0],dirkeypad),position) <= mandist(getcodepos(path2[0][0],dirkeypad),position):
        newins = []
        for i in possibleinstructions:
            if path1good:
                newins.append(i + path1[0] + "A")
            if path2good:
                newins.append(i + path2[0] + "A")
        possibleinstructions = newins
        position = targetpos
        

    return list(set(possibleinstructions))


memopaths = {}

def firsttimepath(postuple):
    position = getcodepos(postuple[0],dirkeypad)
    targetpos = getcodepos(postuple[1],dirkeypad)
    xdir = getxdir(position,targetpos)
    ydir = getydir(position,targetpos)
    xdist = abs(position[0] - targetpos[0])
    ydist = abs(position[1] - targetpos[1])

        #generate both paths to get to button. discard paths that go through X. take first one that doesnt
    #x first
    path1 = ["",[]]
    testpos = position
    if targetpos == position:
        memopaths[postuple] = "A"
        return

    for i in range(xdist):
        testpos = (testpos[0]+xdir,testpos[1]) 
        path1[1].append(testpos)
        if xdir == 1: path1[0] += ">"
        if xdir == -1: path1[0] += "<"
    for i in range(ydist):
        testpos = (testpos[0],testpos[1]+ydir) 
        path1[1].append(testpos)
        if ydir == 1: path1[0] += "^"
        if ydir == -1: path1[0] += "v"
    path2 = ["",[]]
    testpos = position
    for i in range(ydist):
        testpos = (testpos[0],testpos[1]+ydir) 
        path2[1].append(testpos)
        if ydir == 1: path2[0] += "^"
        if ydir == -1: path2[0] += "v"
    for i in range(xdist):
        testpos = (testpos[0]+xdir,testpos[1]) 
        path2[1].append(testpos)
        if xdir == 1: path2[0] += ">"
        if xdir == -1: path2[0] += "<"
    path1good = True
    for item in path1[1]:
        if dirkeypad[item[1]][item[0]] == "X": path1good = False
    path2good = True
    for item in path2[1]:
        if dirkeypad[item[1]][item[0]] == "X": path2good = False
    #if mandist(getcodepos(path1[0][0],dirkeypad),position) <= mandist(getcodepos(path2[0][0],dirkeypad),position):
        possible = []
        if path1good:
            possible.append(path1[0] + "A")
        if path2good:
            possible.append(path2[0] + "A")
        if len(possible) == 1 or possible[0] == possible[1]:
            memopaths[postuple] = possible[0]
        else:
            if possible[0][0] == "<" or possible[0][0] == "^":
                memopaths[postuple] = possible[0]
            else:
                memopaths[postuple] = possible[1]



def memoedkeypad(iterpathsl):
    newiterpathstotallist = []
    for iterpaths in iterpathsl:
        newiterpathslist = []
        newpath = defaultdict(int)
        newiterpathslist.append(newpath)

        for code in iterpaths:
            for idx in range(len(code)):
                if idx == 0:
                    start = "A"
                else:
                    start = code[idx-1]
                end = code[idx]

                pathtuple = (start,end)

                if pathtuple not in memopaths:
                    firsttimepath(pathtuple)

                for state in newiterpathslist:
                    state[memopaths[pathtuple]] += iterpaths[code]
        newiterpathstotallist.extend(newiterpathslist)
    return newiterpathstotallist


def splitup(inp):
    memoed = {}
    parts = inp.split("A")
    for p in parts:
        if p != "":
            memoed[p+"A"] = 1
    return memoed

def getlen(memoed):
    length = 0
    for x in memoed:
        length += len(x) * memoed[x]
    return length



print(getcodepos("0",firstkeypad))
print(genkeypadinputs("029A",firstkeypad))
silver = 0
for code in codes:
    code = code.strip()

    firstcode = genkeypadinputs(code,firstkeypad)
    #keycode = splitup(firstcode)
    keycode = defaultdict(int)
    print("F",firstcode)
    keycode[firstcode[0]] = 1
    keycode = [keycode]
    keycode = []
    for x in firstcode:
        xd = defaultdict(int)
        xd[x] = 1
        keycode.append(xd)
    print(keycode)
    for i in range(25):
        print(i)
        keycode = memoedkeypad(keycode)
        print(len(keycode))
        randsel = []
        #for x in keycode:
        #    print(getlen(x))
        """
        for i in range(1000000):
            randsel.append(keycode[random.randint(0,len(keycode)-1)])
        print(len(keycode))
        keycode = randsel
        #keycode = sorted(keycode,key=lambda x: getlen(x))
        #keycode = keycode[0:100000]
        """
    print(memopaths)


    
    maxlen = 999999999999999999
    for item in keycode:
        ilen = getlen(item)
        if ilen < maxlen:
            maxlen = ilen

    codeint = int(code[0:3])
    silver += maxlen*codeint
print(silver)
