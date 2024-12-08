raw = open("input.txt","r").readlines()

lines = [[x for x in line.strip()] for line in raw]

maxy = len(lines)
maxx = len(lines[0])
antis = set()
antnum = 0
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


                            n = 0
                            a1x = x-dx*n
                            a1y = y-dy*n
                            anti1 = (a1x,a1y)
                            check = True
                            while check:
                                if -1 < a1x and a1x < maxx:
                                    if -1 < a1y and a1y < maxy:

                                        antis.add(anti1)
                                        n += 1
                                        a1x = x-(dx*n)
                                        a1y = y-(dy*n)
                                        anti1 = (a1x,a1y)
                                    else:
                                        check = False
                                else:
                                    check = False
                            check = True
                            n = 0
                            a2x = x2+dx*n
                            a2y = y2+dy*n
                            anti2 = (a2x,a2y)
                            while check:
                                if -1 < a2x and a2x < maxx:
                                    if -1 < a2y and a2y < maxy:
                                        print("A2",anti2,a2x,a2y)
                                        antis.add(anti2)
                                        n += 1
                                        a2x = x2+(dx*n)
                                        a2y = y2+(dy*n)
                                        anti2 = (a2x,a2y)
                                    else:
                                        check = False
                                else:
                                    check = False


print(maxx)
print(maxy)
print(antis)
print(len(antis))
                        

