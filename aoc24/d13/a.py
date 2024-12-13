f = open("input.txt","r").read()
machines = f.split("\n\n")

def add(p1,p2):
    return(p1[0]+p2[0],p1[1]+p2[1])

silver = 0
gold = 0
for m in machines:
    lines = m.split("\n")
    apress = lines[0].split()
    acost = (int(apress[2].split("+")[1].strip(",")),int(apress[3].split("+")[1]))
    bpress = lines[1].split()
    bcost = (int(bpress[2].split("+")[1].strip(",")),int(bpress[3].split("+")[1]))
    prize = lines[2].split()
    prize = (int(prize[1].split("=")[1].strip(",")),int(prize[2].split("=")[1]))
    prize = add(prize,(10000000000000,10000000000000))
    #print(acost,bcost,prize)
    mathb = (prize[1] - (prize[0]*acost[1]/acost[0]))/(bcost[1] - (bcost[0]*acost[1]/acost[0]))
    matha = (prize[0] - mathb*bcost[0])/acost[0]
    if matha > 0 and mathb > 0:
        if round(matha)*acost[0] + round(mathb)*bcost[0] == prize[0]:
            if round(matha)*acost[1] + round(mathb)*bcost[1] == prize[1]:
                gold += matha*3+mathb
print(gold)

            

    
