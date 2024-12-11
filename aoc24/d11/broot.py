from collections import deque
f = open("input.txt","r").read()
stones = [int(x) for x in f.strip().split()]


stack = deque()

for stone in stones:
    stack.append([stone,0])

def brootblink(stones):
    newstones = []
    for s in stones:
        if s == 0:
            newstones.append(1)
        elif(len(str(s))%2 == 0):
            newstones.append(int(str(s)[:int((len(str(s)))/2)]))
            newstones.append(int(str(s)[int((len(str(s)))/2):]))
        else:
            newstones.append(s*2024)
    return newstones


accum = 0
target = 75

while stack:
    stone = stack.pop()
    s = stone[0]
    if stone[1] == target:
        accum += 1
    elif stone[0] == 0:
        stack.append([1,stone[1]+1])
    elif(len(str(s))%2 == 0):
        stack.append([int(str(s)[:int((len(str(s)))/2)]),stone[1]+1])
        stack.append([int(str(s)[int((len(str(s)))/2):]),stone[1]+1])
    else:
        stack.append([s*2024,stone[1]+1])
    if accum % 1000000 == 0:
        print(accum)

print(accum)

