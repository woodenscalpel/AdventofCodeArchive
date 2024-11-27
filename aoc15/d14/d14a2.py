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


time = 2503
#time = 1000

for deer in deers:
    deer = deers[deer]

    burst = deer["speed"]*deer["runtime"]
    bursttime = deer["runtime"]+deer["resttime"]

    number = int(time/bursttime)

    main = number*burst
    
    remaindertime = time - bursttime*number
    if remaindertime > deer["runtime"]:
        print((number+1)*burst)
    else:
        print((number)*burst+(remaindertime*deer["speed"]))
