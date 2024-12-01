import re

lines = open("input.txt","r").readlines()

ans = 0
for line in lines:
    line = re.split("\\[|\\]",line.strip())
    inb = False
    outb = False
    for idx, s in enumerate(line):
        print(s)
        for cidx in range(len(s)-3):
            if(s[cidx] == s[cidx+3] and s[cidx+1] == s[cidx+2] and s[cidx] != s[cidx + 1]):
                if(idx % 2 == 0):
                    outb = True
                else:
                    inb = True
                #print(s[cidx:cidx+4])
            #print(s[cidx])
    if outb and not inb:
        ans += 1
print(ans)
