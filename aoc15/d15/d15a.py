cookies = [[5,-1,0,0,5],
           [-1,3,0,0,1],
           [0,-1,4,0,6],
           [-1,0,0,2,8]]

def score(a,b,c,d):
    totalc = max(cookies[0][0]*a + cookies[1][0]*b + cookies[2][0]*c + cookies[3][0]*d,0)
    totald = max(cookies[0][1]*a + cookies[1][1]*b + cookies[2][1]*c + cookies[3][1]*d,0)
    totalf = max(cookies[0][2]*a + cookies[1][2]*b + cookies[2][2]*c + cookies[3][2]*d,0)
    totalt = max(cookies[0][3]*a + cookies[1][3]*b + cookies[2][3]*c + cookies[3][3]*d,0)
    return totalc*totald*totalf*totalt

def cals(a,b,c,d):
    return max(cookies[0][4]*a + cookies[1][4]*b + cookies[2][4]*c + cookies[3][4]*d,0)
maxscore = 0

for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            for d in range(101-a-b-c):
                nscore = score(a,b,c,d)
                if nscore > maxscore: 
                    if cals(a,b,c,d) == 500:
                        maxscore = nscore

print(maxscore)
