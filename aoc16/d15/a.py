#discsizes = [5,2]
#discpos = [4,1]
discsizes = [13,5,17,3,7,19,11]
discpos = [11,0,11,0,2,17,0]

t = 0
while True:
    simdiscpos = []
    for d in range(len(discsizes)):
        simdiscpos.append((discpos[d]+ d+1) % discsizes[d])
    #print(simdiscpos)
    correct = True
    for x in simdiscpos:
        if x != 0:
            correct = False
    if correct: 
        print(t)
        input()
    t +=1
    for d in range(len(discsizes)):
        discpos[d] = (discpos[d]+1)%discsizes[d]

