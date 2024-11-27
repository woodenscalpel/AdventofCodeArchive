lines = open("input.txt","r").read()[:-1].split("\n")

memo = {}
        
def getval(ident):

    if(ident in memo):
        return memo[ident]

    try:
        int(ident)
        memo[ident] = int(ident)
        return int(ident)
    except:
        pass

    for line in lines:
        line = line.split()
        if line:
            output = line[-1]
            inp = line[:-2]

            if output == ident:
                if len(inp) == 1:
                    memo[ident] = getval(inp[0])
                    return getval(inp[0])

                elif inp[0] == "NOT":
                    memo[ident] =  ~getval(inp[1])
                    return ~getval(inp[1])
                elif inp[1] == "OR":
                    memo[ident]= getval(inp[0]) | getval(inp[2])
                    return getval(inp[0]) | getval(inp[2])
                elif inp[1] == "AND":
                    memo[ident] = getval(inp[0]) & getval(inp[2])
                    return  getval(inp[0]) & getval(inp[2])

                elif inp[1] == "RSHIFT":
                    memo[ident] =   getval(inp[0]) >> getval(inp[2])
                    return  getval(inp[0]) >> getval(inp[2])
                elif inp[1] == "LSHIFT":
                    memo[ident] =  getval(inp[0]) << getval(inp[2])
                    return getval(inp[0]) << getval(inp[2])


print(getval('a'))
