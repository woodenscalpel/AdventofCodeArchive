f = open("input.txt","r").read().strip()

print(f)
acc = 0
for p in range(len(f)):
    #print(idx,char)
    if f[p:p+4] == 'mul(':
        print(f[p:p+4])
        p = p+4
        inst = ""
        while(f[p] != ")"):

            #print(f[p])
            inst += f[p]
            p += 1
        print("i",inst)
        try:
            inst = inst.split(",")
            if len(inst[0]) == len(inst[0].strip()):
                if len(inst[1]) == len(inst[1].strip()):
                    add = int(inst[0])*int(inst[1])
                    print(add)
                    acc += int(inst[0])*int(inst[1])
        except:
            pass
print(acc)

import re

pattern = "mul\(\d+,\d+\)"
regexpattern = re.compile(pattern)
acc = 0
for p in regexpattern.findall(f):
    nums = p[4:-1]
    nums = nums.split(",")
    print(nums)
    acc += int(nums[0])*int(nums[1])
print(acc)


goodstring = ""
lookfordont = True
pstart = 0
for p in range(len(f)):
    #print(idx,char)
    if lookfordont:
        if f[p:p+6] == "don't(":
            goodstring += f[pstart:p]
            lookfordont = False
            print("DONT")
    else:
        if f[p:p+3] == "do(":
            lookfordont = True
            pstart = p
if lookfordont == True:
    goodstring += f[pstart:]


print(goodstring)
acc = 0 
for p in regexpattern.findall(goodstring):
    nums = p[4:-1]
    print(nums)
    nums = nums.split(",")
    acc += int(nums[0])*int(nums[1])
print(acc)
