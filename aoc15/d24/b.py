import copy
from itertools import combinations
lines = [int(i) for i in open("input.txt","r").readlines()]

packages = list(reversed(lines))

target = sum(lines)/4 #each bag needs a third
print(target)


def grabn(n,packages):
    return combinations(packages,n)

def remainingbagsbalanced(bag,packages):
    p = packages.copy()
    for b in bag:
        p.remove(b)
    for n in range(len(p)):
        for c in list(combinations(p,n)):
            if sum(c) == target:
                return True
    return False


def quantum(bag):
    prod = 1
    for x in bag:
        prod = prod*x
    return prod





for leftamount in range(len(packages)): # start with smallest amount of packages
    #start with largest package as to minimize number
    possiblebags = list(grabn(leftamount,packages))
    quantums = [999999999999999999999999999]
    for bag in possiblebags:
        if sum(bag) == target:
            if remainingbagsbalanced(bag,packages):
                print(bag)
                print(leftamount)
                print(quantum(bag))
                quantums.append(quantum(bag))
    print("min: ",min(quantums))
    input()
    
    
    
