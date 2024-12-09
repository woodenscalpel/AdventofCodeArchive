f = open("input.txt","r").read().strip()
compressed = [int(x) for x in f]
uncompressed = []

fileid = 0
i = 0
while i < len(compressed):
    uncompressed.extend(compressed[i]*[str(fileid)])
    i +=1
    if(i == len(compressed)):
        break
    uncompressed.extend(compressed[i]*["."])
    fileid +=1
    i += 1
golduncompressed = uncompressed.copy()

bp = 0 #beginning pointer
ep = len(uncompressed)-1 # end pointer

while bp < ep: #I think this works
    #find thing to move from end
    while uncompressed[ep] == ".":
        ep -= 1
    #find next free from beginning
    while uncompressed[bp] != ".":
        bp += 1
    #mutate
    if bp <= ep:
        uncompressed =uncompressed[:bp] + [uncompressed[ep]] + uncompressed[bp+1:ep] +uncompressed[ep+1:]
        """
    else: 
        uncompressed =uncompressed[:bp] + uncompressed[bp+1:ep] +uncompressed[ep+1:]
        """
    ep -= 1

#checksum
silver = 0
for idx in range(len(uncompressed)):
    if uncompressed[idx] != ".":
        silver += int(uncompressed[idx])*idx
print(silver)


fileid = 0
i = 0
uncompressed = []
while i < len(compressed):
    uncompressed.append([fileid,compressed[i]])
    i+=1
    if(i == len(compressed)):
        break
    if compressed[i] != 0:
        uncompressed.append([".",compressed[i]])
    i+=1
    fileid += 1

print(uncompressed)
print(len(uncompressed))
#input()
bp = 0 #beginning pointer

def consolidatespaces(uncompressed):
    newlist = []
    idx = 0
    while idx < len(uncompressed):
        if uncompressed[idx][0] != ".":
            newlist.append(uncompressed[idx])
            idx +=1
        else:
            free = 0
            while uncompressed[idx][0] == ".":
                free += uncompressed[idx][1]
                idx += 1
                if idx > len(uncompressed)-1:
                    break
            newlist.append([".",free])
    return newlist


ep = len(uncompressed)-1

lastmoved = 9999999999999999999999999999999999999
while ep > -1:
    #print(uncompressed)
    #input()
    #print("L",len(uncompressed))
    #find thing to move from end
    #find next free from beginning
    #print(bp,uncompressed[bp])

    while uncompressed[ep][0] == ".":
        ep -= 1

    bp = 0

    filled = False
    while(bp < ep) and not filled:
        while uncompressed[bp][0] != ".":
            bp += 1
        freesize = uncompressed[bp][1]

        if (uncompressed[ep][1] <= freesize) and (ep>bp) and (uncompressed[ep][0] < lastmoved):
            #mutate
            lastmoved = uncompressed[ep][0]
            if(freesize-uncompressed[ep][1] > 0):
                mutated = [uncompressed[ep],[".",freesize-uncompressed[ep][1]]]
            else:
                mutated = [uncompressed[ep]]
            oldlen = len(uncompressed)
            uncompressed = uncompressed[:bp] + mutated + uncompressed[bp+1:ep] + [[".",uncompressed[ep][1]]] + uncompressed[ep+1:]
            ep += 1 #### NOT ADDING THIS LINE CAUSED 40 MINUTES OF DEBUGGING????????
            ep = min(len(uncompressed),ep)
            filled = True
        else:
            bp +=1
    ep -=1

print(uncompressed)



gold = 0
idx = 0
for item in uncompressed:
    for i in range(item[1]):
        if item[0] != ".":
            gold += idx*item[0]
        idx += 1
print(gold)
