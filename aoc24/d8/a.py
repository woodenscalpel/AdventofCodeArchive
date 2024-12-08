raw = open("input.txt","r").readlines()

lines = [[x for x in line.strip()] for line in raw]

maxy = len(lines)
maxx = len(lines[0])
antis = set()
for y,row in enumerate(lines):
    for x,char in enumerate(row):
        if char != ".":
            for y2,row2 in enumerate(lines):
                for x2,char2 in enumerate(row2):
                    if char == char2:
                        if x != x2 and y != y2:
                            print(char,char2)
                            #print("antenna match")
                            dy = (y2-y)
                            dx = (x2-x)
                            a1x = x-dx
                            a1y = y-dy

                            a2x = x2+dx
                            a2y = y2+dy

                            anti1 = (x-dx,y-dy)
                            anti2 = (x2+dx,y2+dy)
                            print(x,y,x2,y2,anti1,anti2)

                            if -1 < a1x and a1x < maxx:
                                if -1 < a1y and a1y < maxy:
                                    antis.add(anti1)
                            if -1 < a2x and a2x < maxx:
                                if -1 < a2y and a2y < maxy:
                                    antis.add(anti2)

print(maxx)
print(maxy)
print(antis)
print(len(antis))
                        

