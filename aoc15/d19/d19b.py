replacements = [["Al" ,"ThF"],
["Al" ,"ThRnFAr"],
["B","BCa"],
["B","TiB"],
["B","TiRnFAr"],
["Ca","CaCa"],
["Ca","PB"],
["Ca","PRnFAr"],
["Ca","SiRnFYFAr"],
["Ca","SiRnMgAr"],
["Ca","SiTh"],
["F","CaF"],
["F","PMg"],
["F","SiAl"],
["H","CRnAlAr"],
["H","CRnFYFYFAr"],
["H","CRnFYMgAr"],
["H","CRnMgYFAr"],
["H","HCa"],
["H","NRnFYFAr"],
["H","NRnMgAr"],
["H","NTh"],
["H","OB"],
["H","ORnFAr"],
["Mg","BF"],
["Mg","TiMg"],
["N","CRnFAr"],
["N","HSi"],
["O","CRnFYFAr"],
["O","CRnMgAr"],
["O","HP"],
["O","NRnFAr"],
["O","OTi"],
["P","CaP"],
["P","PTi"],
["P","SiRnFAr"],
["Si","CaSi"],
["Th","ThCa"],
["Ti","BP"],
["Ti","TiTi"],
["e","HF"],
["e","NAl"],
["e","OMg"]]

start = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"

#replacements = [["e","H"],["e","O"],["H","HO"],["H","OH"],["O","HH"]]
#start = "HOHOHO"

replacements = [list(reversed(x)) for x in replacements]
print(replacements)

def doreplace(molecule,replacements):
    newlist = []
    for replacement in replacements:
        lrep = len(replacement[0])
        for idx in range(len(molecule)-lrep+1):
            check = molecule[idx:idx+lrep]
            #print(check, replacement[0])
            if check == replacement[0]:
                new = molecule[:idx] + replacement[1] + molecule[idx+lrep:]
                newlist.append(new)
    return(set(newlist))

nreps = 0
found = False
mollist = [start]
while not found:
    newlist = set()
    for mol in list(mollist)[0:1]: #Depth first search and cross fingers
        ret = doreplace(mol,replacements)
        newlist.update(doreplace(mol,replacements))
        if mol == "e":
            found = True
            print("ANS: ", nreps)
    mollist = newlist
    nreps +=1
    print(nreps)
    print(len(mollist))

#print(len(start))
