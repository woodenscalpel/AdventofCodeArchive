row = 3010
col = 3019


def codenum(row,col):
    startnum = 1
    for c in range(1,col):
        startnum +=c
    #print(startnum)
    for r in range(1,row):
        startnum += (col+r)

    #print(startnum)
    return startnum


def code(codeidx):
    code =20151125
    for i in range(codeidx-1):
        code = code*252533 % 33554393
    return code


print(codenum(1,2))
print(code(codenum(col,row)))
