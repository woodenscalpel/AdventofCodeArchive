f = open("test2.txt","r").read().strip()
compressed = [int(x) for x in f]
print(compressed)
uncompressed = ""

fileid = 0
i = 0
while i < len(compressed):
    uncompressed += compressed[i]*str(fileid)
    i +=1
    if(i == len(compressed)):
        break
    uncompressed += compressed[i]*"."
    fileid +=1
    i += 1
print(uncompressed)
uncompressed += "....."

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
    #print(uncompressed[:bp],uncompressed[bp:ep],uncompressed[ep:])
    #print(uncompressed[:bp],uncompressed[ep],uncompressed[bp+1:ep],uncompressed[ep+1:])
    if bp <= ep:
        uncompressed =uncompressed[:bp] + uncompressed[ep] + uncompressed[bp+1:ep] +uncompressed[ep+1:]
        """
    else: 
        uncompressed =uncompressed[:bp] + uncompressed[bp+1:ep] +uncompressed[ep+1:]
        """
    ep -= 1
    #print(bp)
uncompressed = uncompressed.strip(".")
print(uncompressed)

#checksum
silver = 0
for idx in range(len(uncompressed)):
#    print(idx,uncompressed[idx])
    silver += int(uncompressed[idx])*idx
print("S")
print(silver)

