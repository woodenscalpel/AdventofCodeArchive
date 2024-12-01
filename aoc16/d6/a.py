lines = open("input.txt","r").readlines()

ans = []
for n in range(len(lines[0])-1):
    ans.append("")
print(ans)
for line in lines:
    line = line.strip()
    for idx, c in enumerate(line):
        ans[idx] += c
print(ans)

ans2 = ""
for digit in ans:
    charcount = {}
    for c in digit:
        if c not in charcount:
            charcount[c] = 0
        charcount[c] += 1

    print(sorted(charcount, key = lambda x: charcount[x]))
    #print(charcount)

