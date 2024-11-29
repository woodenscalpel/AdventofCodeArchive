import math
total = 150
containers = [43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38]

def numcombos(amt,cnts,selected):
    combos = set()
    for i in cnts:
        if amt - i == 0:
            selcopy = selected[:]
            selcopy.append(i)
            combos.add(tuple(sorted(selcopy)))
        if amt - i > 0:
            cntscopy = cnts[:]
            cntscopy.remove(i)

            selcopy = selected[:]
            selcopy.append(i)
            
            combos.update(numcombos(amt-i,cntscopy,selcopy))
    return combos
        


#combos = numcombos(25,[20,15,10,5,5,1,1,1,1,1,3,3,3,3],[])
#containers = [20,15,10,5,5,1,1,1,1,1,3,3,3,3,3]
combos = numcombos(150,containers,[])


totalcombos = 0
for combo in combos:
    add = 1
    for item in combo:
        n = containers.count(item)
        k = combo.count(item)
        add = add*(math.factorial(n)/(math.factorial(k)*(math.factorial(n-k))))
    totalcombos+= add
print(totalcombos)
