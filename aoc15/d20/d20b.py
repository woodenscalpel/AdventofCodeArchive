import math
target = 29000000

def present(N):
    p = 0
    for i in range(1,int(math.sqrt(N))+1):
            if N%i == 0:
                if N / i == i:

                    if(i*50 >= N):
                        p += 11*i
                else:
                    if(i*50 >= N):
                        p += 11*i
                    if(int(N/i)*50 >= N):
                        p += 11*int(N/i)
    return p

for i in range(1000000000):
    if present(i) > target:
        print(i)
