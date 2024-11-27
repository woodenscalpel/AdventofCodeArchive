infile = open("input.txt","r")
strings = infile.read().split()



nicecount = 0

for s in strings:
    hasPair = False
    skipPair = False

    for idx,x in enumerate(s):
        if idx < len(s)-2:
            if x == s[idx+2]:
                skipPair = True
                
        if idx < len(s)-1:
            #print(s)
            #print(s[idx:idx+2])
            #print(s[idx+1:])
            if s[idx:idx+2] in s[idx+2:]:
                hasPair = True
    if hasPair and skipPair: nicecount += 1

print(nicecount)
