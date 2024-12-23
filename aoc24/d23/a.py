from collections import defaultdict
import itertools
f = open("input.txt","r").readlines()


connections = defaultdict(list)
for conn in f:
    conn = conn.strip().split("-")
    if conn[1] not in connections[conn[0]]:
        connections[conn[0]].append(conn[1])
        connections[conn[1]].append(conn[0])

triplets = []
for c in connections:
    if c[0] == "t":
        for possibletriplet in itertools.permutations(connections[c],2):
            if c in connections[possibletriplet[0]]:
                if possibletriplet[1] in connections[possibletriplet[0]]:
                    if c in connections[possibletriplet[1]]:
                        if possibletriplet[0] in connections[possibletriplet[1]]:
                            trip = set([c,possibletriplet[0],possibletriplet[1]])
                            if trip not in triplets:
                                triplets.append(trip)
silver = len(triplets)
print(silver)

#try to expand group by 1
sets = triplets
while len(sets) > 1:
    newsets = []
    for trip in sets:
        #print(trip,list(trip)[0])
        for con in connections[list(trip)[0]]:
            if con not in trip:
                good = True
                for t in trip:
                    if con not in connections[t]:
                        good = False
                if good:
                    trip.add(con)
                    newsets.append(trip)
    if newsets == []:
        maxlen = 0
        finalsets = []
        for s in sets:
            if len(s) > maxlen:
                maxlen = len(s)
                finalsets = s
    sets = newsets
print(",".join(sorted(list(finalsets))))
