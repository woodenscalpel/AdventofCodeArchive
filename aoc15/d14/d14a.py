lines = open("test2.txt","r").readlines()

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


time = 2503
#time = 1000



while time:
    print(deers)
    for deer in deers:
        deer = deers[deer]
        deer["timer"] -= 1
        if deer["running"]:
            if deer["timer"] >= 0:
                deer["distance"] += deer["speed"]
            else:
                deer["running"] = False
                deer["timer"] = deer["resttime"]
        else:
            if deer["timer"] <= 1:
                deer["running"] = True
                deer["timer"] = deer["runtime"]

    time -=1

maxd = 0
for x in deers:
    if deers[x]["distance"] > maxd: maxd = deers[x]["distance"]
print(maxd)
