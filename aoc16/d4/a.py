lines = open("input.txt","r").readlines()

lines = [line.split("-") for line in lines]

for l in lines:
    l[-1] = l[-1].split("[")
    l[-1][-1] = l[-1][-1].strip("]\n")
    l[-1][0] = int(l[-1][0])


ans = 0
for l in lines:
    data = l[:-1]
    meta = l[-1]
    chardict = {}
    for s in data:
        for c in s:
            if c not in chardict:
                chardict[c] = 0
            chardict[c] += 1
    most = "".join([y[0] for y in list(reversed(sorted(chardict.items(),key=lambda x: (x[1],ord(x[0])*-1))))[:5]])
    if most == meta[1]:
        ans += meta[0]

    print(data,meta)
print(ans)
