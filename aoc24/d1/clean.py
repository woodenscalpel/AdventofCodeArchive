sorteddata = [sorted(i) for i in list(zip(*[x.split() for x in open("input.txt","r").readlines()]))]
print(sum([abs(int(x)-int(y)) for x,y in zip(*sorteddata)]))
print(sum([int(i) for i in sorteddata[1] for n in sorteddata[0] if i == n]))
