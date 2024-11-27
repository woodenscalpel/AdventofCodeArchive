lines = open("input.txt","r").readlines()
print(lines)

locations = {}
for line in lines:
    line = line.split()
    if line[0] in locations:
        locations[line[0]][line[2]] = line[4]
    else:
        locations[line[0]] = {}
        locations[line[0]][line[2]] = line[4]

    if line[2] in locations:
            locations[line[2]][line[0]] = line[4]
    else:
            locations[line[2]] = {}
            locations[line[2]][line[0]] = line[4]



Nloc = len(locations)
currentlist = [[[k],0] for k in locations.keys()]

print(currentlist)

def iteratewalk(currentlist):
    nextlist = []
    for route,dist in currentlist:

        for connection,conndist in locations[route[-1]].items():
            if connection not in route:
                newroute = [ route + [connection],dist+int(conndist) ]
                nextlist.append(newroute)
    return nextlist



for i in range(Nloc-1):
 currentlist = iteratewalk(currentlist)

print(currentlist)

mind = 999999999999
maxd = 0
for item,d in currentlist:
    if len(item) == Nloc:
        if d < mind: mind = d
        if d > maxd: maxd = d
#print(currentlist)
print(mind)
print(maxd)

