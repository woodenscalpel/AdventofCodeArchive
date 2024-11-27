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
        print(line[x])
        if line[x] == "\\":
            if line[x+1] == "x":
                x+=3
                skip +=0
            else:
                x += 1
                skip += 0
        x=x+1

        parse += 1
    print(raw)
    print(parse-skip)
    print(" ")
    total+=raw
    totals += (parse-skip)

print(total)
print(totals)
print(total-totals)
