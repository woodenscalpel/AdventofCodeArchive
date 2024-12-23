import hashlib
#salt = "abc" 
salt = "ihaygndm"
hashlib.md5()


data = []
keys = []
threes = []
fives = []
for x in range(10000000000000000):
    string = salt + str(x)
    h = hashlib.md5(string.encode("utf-8")).hexdigest()
    repeats = 0
    foundthree = False
    for i in range(1,len(h)):
        if h[i] == h[i-1]:
            repeats += 1
        else:
            repeats = 0
        if repeats == 2 and not foundthree:
            threes.append((x,h[i]))
            foundthree = True
        if repeats == 4:
            fives.append((x,h[i]))
            for t in threes:
                if t[1] == h[i]:
                    if t[0] > x-1000 and t[0] != x and t[0] not in keys:
                        keys.append(t[0])
                        #print(x,t[0])
                        #print(sorted(keys))
                        keys.sort()
                        if len(keys) > 64:
                            if x > keys[63] +1000:
                                print(keys)
                                print(keys[63])
                                input()




    
