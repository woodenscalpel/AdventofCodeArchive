lines = open("input.txt","r").readlines()

deers = {}

for line in lines:
    line = line.split()
    deers[line[0]] = {}
    deers[line[0]]["speed"] = int(line[3])
    deers[line[0]]["runtime"] = int(line[6])
    deers[line[0]]["resttime"] = int(line[13])
    deers[line[0]]["running"] = True
    deers[line[0]]["timer"] = deers[line[0]]["runtime"]
    deers[line[0]]["distance"] = 0
    deers[line[0]]["points"] = 0


time = 2503
#time = 1001



while time:
    print(deers)
    for deer in deers:
        deer = deers[deer]

        if deer["running"]:
            if deer["timer"] > 1:
                deer["distance"] += deer["speed"]
            if deer["timer"] == 1:
                deer["distance"] += deer["speed"]
                deer["running"] = False
                deer["timer"] = deer["resttime"]+1
        else:
            if deer["timer"] == 1:
                deer["running"] = True
                deer["timer"] = deer["runtime"]+1
        deer["timer"] -= 1

    bestdeer = None
    bestdist = 0
    for deer in deers:
        if deers[deer]["distance"] > bestdist:
            bestdist = deers[deer]["distance"]
            bestdeer = deer
    deers[bestdeer]["points"] +=1
    

    time -=1

maxd = 0
for x in deers:
    if deers[x]["points"] > maxd: maxd = deers[x]["points"]
print(maxd)
