lines = open("input.txt","r").read().split()

total = 0
totals = 0
for line in lines:
    raw = len(line)
    skip = 0

    parse = 0
    skip = 2
    x=0
    while x < len(line):
        #print(line[x])
        if line[x] == "\\":
                skip +=1
        if line[x] == "\"":
            skip += 1
        x=x+1

        parse += 1
    print(raw)
    print(parse+skip)
    print(" ")
    total+=raw
    totals += (parse+skip)

print(total)
print(totals)
print(totals-total)
