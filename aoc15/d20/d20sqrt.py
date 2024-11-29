import math
target = 29000000

def present(N):
    p = 0
    for i in range(1,int(math.sqrt(N))+1):
        if N%i == 0:
            if N / i == i:
                p += 10*i
            else:
                p += 10*i
                p += 10*int(N/i)
    return p

for i in range(1000000000):
    if present(i) > target:
        print(i)
