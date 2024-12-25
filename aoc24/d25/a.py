f = open("input.txt","r").read()

items = f.strip().split("\n\n")

print(items)


def readlock(lock):
    lock = lock.split("\n")
    print(lock)
    teeth = [-1,-1,-1,-1,-1]
    for row in lock:
        for idx,char in enumerate(row):
            if char == "#":
                teeth[idx] += 1
    return teeth

def readkey(key):
    return readlock(key)

keys = []
locks = []
for item in items:
    if item[0] == "#":
        locks.append(readlock(item))
    if item[0] == ".":
        keys.append(readkey(item))

silver = 0
for key in keys:
    for lock in locks:
        good = True
        for i in range(5):
            if key[i] + lock[i] > 5:
                good = False
        if good:
            silver += 1
print(silver)
