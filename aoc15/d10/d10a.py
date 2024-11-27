from collections import deque
start = deque(list("1113222113"))
start = list("1113222113")
start = [int(s) for s in start]

print(start)


def nextn(number):
    nextnumber = []
    
    prevnumber = 0
    ncount = 1
    for n in number:
        if prevnumber == n:
            ncount += 1
        else:
            nextnumber.append(ncount+1)
            nextnumber.append(prevnumber)
            ncount = 0
        prevnumber = n

    nextnumber.append(ncount+1)
    nextnumber.append(prevnumber)
    return nextnumber[2:]

for i in range(50):
    start = nextn(start)
    #print(start)
print(len(start))
