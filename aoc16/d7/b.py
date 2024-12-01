import re
import itertools


lines = open("input.txt","r").readlines()

ans = 0
for line in lines:
    line = re.split("\\[|\\]",line.strip())
    inb = []
    outb = []
    supports = False
    for idx, s in enumerate(line):
        print(s)
        for cidx in range(len(s)-2):
            if(s[cidx] == s[cidx+2] and s[cidx] != s[cidx + 1]):
                if(idx % 2 == 0):
                    outb.append(s[cidx:cidx+3])
                else:
                    inb.append(s[cidx:cidx+3])
                #print(s[cidx:cidx+4])
            #print(s[cidx])
        print(inb,outb)
    for a in inb:
        for b in outb:
            if(a[0] == b[1] and a[1] == b[0]):
                print(a,b)
                supports = True
    if supports:
        ans += 1

print(ans)
