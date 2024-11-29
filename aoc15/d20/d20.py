target = 29000000

def present(N):
    p = 0
    for i in range(1,N+1):
        if N%i == 0:
            p += 10*i
    return p

for i in range(600000,1000000):
    #print(present(i))
    if present(i) > target:
        print(i)
