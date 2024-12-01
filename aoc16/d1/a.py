directions = open("input.txt","r").read()
directions = [ [x.strip()[0],int(x.strip()[1:])] for x in directions.split(",")]
print(directions)

NS = 0
EW = 0

h = "N"
visited = set()

def rotateL(d):
    if d == "N":
        return "W"
    if d == "S":
        return "E"
    if d == "E":
        return "N"
    if d == "W":
        return "S"

def rotateR(d):
    if d == "N":
        return "E"
    if d == "S":
        return "W"
    if d == "E":
        return "S"
    if d == "W":
        return "N"

for d in directions:
    if d[0] == "L":
        h = rotateL(h)
    if d[0] == "R":
        h = rotateR(h)
    
    if h == "N":
        for i in range(1,d[1]):
            if (NS+i,EW) in visited:
                print(abs(NS+i) + abs(EW))
                input()
            visited.add((NS+i,EW))
        NS += d[1]
    if h == "S":
        for i in range(1,d[1]):
            if (NS-i,EW) in visited:
                print(abs(NS-i) + abs(EW))
                input()
            visited.add((NS-i,EW))
        NS -= d[1]
    if h == "E":
        for i in range(1,d[1]):
            if (NS,EW+i) in visited:
                print(abs(NS) + abs(EW+i))
                input()
            visited.add((NS,EW+i))
        EW += d[1]
    if h == "W":
        for i in range(1,d[1]):
            if (NS,EW-i) in visited:
                print(abs(NS) + abs(EW-i))
                input()
            visited.add((NS,EW-i))
        EW -= d[1]
    print(NS,EW)
    print(visited)
    if (NS,EW) in visited:
        print(abs(NS) + abs(EW))
        input()
    else:
        visited.add((NS,EW))
    

print(NS+EW)
