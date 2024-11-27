infile = open("input.txt","r")
strings = infile.read().split()


nicecount = 0

for s in strings:
    vowels = 0
    threevowels = False
    double = False
    isnice = False
    forbidden = False

    for idx,x in enumerate(s):
        if(x in "aeiou"):
            vowels +=1
            if vowels > 2:
                threevowels = True
        try:
            if s[idx+1] == x:
                double = True
        except:
            pass
        if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
            forbidden = True
            break;

    print(s)
    print(threevowels)
    print(double)
    print(forbidden)
    if threevowels and double and not forbidden : nicecount += 1

print(nicecount)
