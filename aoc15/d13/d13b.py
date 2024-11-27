import itertools

lines = open("input.txt","r").readlines()

connections = {}

for line in lines:
    line = line.split()
    person = line[0]
    happiness = int(line[3])
    if line[2] == "lose": happiness = 0-int(happiness)
    neighbour = line[-1][:-1]
    
    if person not in connections:
        connections[person] = {}
    connections[person][neighbour] = happiness


people = connections.keys()
N = len(people)

connections["me"] = {}
for person in connections.keys():
    connections[person]["me"] = 0
    connections["me"][person] = 0

people = connections.keys()
N = len(people)


possible = itertools.permutations(people)

best = 0
for item in possible:
    score = 0
    for i in range(1,N-1):
        score += connections[item[i]][item[i-1]] + connections[item[i]][item[i+1]]
    score += connections[item[0]][item[N-1]] + connections[item[0]][item[1]]
    score += connections[item[N-1]][item[N-2]] + connections[item[N-1]][item[0]]
    if score > best: best = score
print(best)
        #print(i)
