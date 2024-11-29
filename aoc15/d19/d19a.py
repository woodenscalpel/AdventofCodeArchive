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

#replacements = [["abc","def"]]
#start = "123abc456abc789"

newlist = []

for replacement in replacements:
    lrep = len(replacement[0])
    for idx in range(len(start)-lrep+1):
        check = start[idx:idx+lrep]
        #print(check, replacement[0])
        if check == replacement[0]:
            new = start[:idx] + replacement[1] + start[idx+lrep:]
            newlist.append(new)
            #print(new)
print(len(set(newlist)))

print(len(start))
