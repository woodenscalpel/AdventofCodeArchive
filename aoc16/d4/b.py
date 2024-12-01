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
        word = ""
        for c in s:
            chord = ord(c)
            for i in range(meta[0]):
                chord += 1
                if chord > ord('z'):
                    chord = ord('a')

            word += (chr(chord))
        #print(word)
        if word == "northpole":
            print(meta[0])

    #print(data,meta)
