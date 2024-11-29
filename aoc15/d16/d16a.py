sues = {}
target = [["children:", 3]
,["cats:", 7]
,["samoyeds:", 2]
,["pomeranians:", 3]
,["akitas:", 0]
,["vizslas:", 0]
,["goldfish:", 5]
,["trees:", 3]
,["cars:", 2]
,["perfumes:", 1]
          ]
for line in open("input.txt","r").readlines():
    line = line.split()
    name = line[1]
    thing1 = line[2]
    thing2 = line[4]
    thing3 = line[6]
    num1 = int(line[3].strip(","))
    num2 = int(line[5].strip(","))
    num3 = int(line[7].strip(","))
    sues[name] = {}
    sues[name][thing1] = num1
    sues[name][thing2] = num2
    sues[name][thing3] = num3




for sue in sues:
    correct = True
    for t in target:
        if t[0] in sues[sue]:
            if t[0] == "cats:" or t[0] == "trees:":
                if sues[sue][t[0]] <= t[1]:
                    correct = False
            elif t[0] == "pomeranians:" or t[0] == "goldfish:":
                if sues[sue][t[0]] >= t[1]:
                    correct = False
            elif sues[sue][t[0]] != t[1]:
                correct = False
    if correct:
        print(sue)
