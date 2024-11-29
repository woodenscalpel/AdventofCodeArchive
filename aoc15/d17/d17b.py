import math
total = 150
containers = [43,3,4,10,21,44,4,6,47,41,34,17,17,44,36,31,46,9,27,38]

def numcombos(amt,cnts,selected):
    combos = []

    if len(cnts) == 0:
        return []

    first = cnts[0]
    rest = cnts[1:]
    
    #With first
    wfamt = amt - first
    newfselected = selected[:] + [first]
    combos += numcombos(wfamt,rest,newfselected)
    if wfamt == 0:
        combos += [newfselected]
    
    #without first
    combos += numcombos(amt,rest,selected)
    
    return combos
        

#total = 25
#containers = [20,15,10,5,5]

combos = numcombos(total,containers,[])
print(len(combos))

minlen = 999
amt = 0
for combo in combos:
    if len(combo) == minlen:
        amt += 1
    if len(combo) < minlen:
        amt = 1
        minlen = len(combo)
print(amt)
