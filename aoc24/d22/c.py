from collections import defaultdict
f = open("input.txt","r").readlines()


def nextsecret(num):
    num2 = num*64
    mixresult = mix(num,num2)
    num = prune(mixresult)

    num2 = int(num/32)
    mixresult = mix(num,num2)
    num = prune(mixresult)

    num2 = num*2048
    mixresult = mix(num,num2)
    num = prune(mixresult)

    return num


def mix(n1,n2):
    return n1 ^ n2

def prune(n1):
    return n1 % 16777216


silver = 0
monkeydata = []
for secret in f:
    secret = int(secret)
    prices = []
    diffs = []
    diffmap = defaultdict(int)
    prices.append(int(str(secret)[-1]))
    for i in range(2000):
        secret = nextsecret(secret)
        prices.append(int(str(secret)[-1]))
        diffs.append(prices[i] - prices[i-1])
        if i > 3:
            if (diffs[i-3],diffs[i-2],diffs[i-1],diffs[i]) not in diffmap:
                diffmap[(diffs[i-3],diffs[i-2],diffs[i-1],diffs[i])] = prices[i]
    monkeydata.append(diffmap)

    silver += secret
print(silver)
#print(monkeydata)
"""
testtarget = (-2,1,-1,3)
for monkey in monkeydata:
    banana = monkey[testtarget]
    print(banana)
input()
"""

maxbananas = 0
ti = 0
for c1 in range(-9,10):
    for c2 in range(-9,10):
        for c3 in range(-9,10):
            for c4 in range(-9,10):
                target = (c1,c2,c3,c4)
                ti +=1
                if ti % 10000 == 0:
                    print("iteration number: ",ti)
                
                bananas = 0
                for monkey in monkeydata:
                    if target in monkey:
                        bananas += monkey[target]
                if bananas > maxbananas:
                    maxbananas = bananas
                    print("max: ", maxbananas)
print(maxbananas)
