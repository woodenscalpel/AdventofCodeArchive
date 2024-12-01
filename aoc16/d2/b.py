instructions = open("input.txt","r").readlines()
ins = [x.strip() for x in instructions]


pos = [-2,0] #x,y

for i in ins:
    for c in i:
        if(pos == [2,0]):
            if c == "L": pos = [1,0]

        elif(pos == [0,2]):
            if c == "D": pos = [0,1]

        elif(pos == [0,-2]):
            if c == "U": pos = [0,-1]

        elif(pos == [-2,0]):
            if c == "R": pos = [-1,0]
        else:

            if c == "L":
                if(pos == [-1,0]):
                    pos = [-2,0]
                else:
                    pos[0] = max(-1, pos[0]-1)
            if c == "D":
                if(pos == [0,-1]):
                    pos = [0,-2]
                else:
                    pos[1] = max(-1, pos[1]-1)
            if c == "U":
                if(pos == [0,1]):
                    pos = [0,2]
                else:
                    pos[1] = min(1, pos[1]+1)
            if c == "R":
                if(pos == [1,0]):
                    pos = [2,0]
                else:
                    pos[0] = min(1, pos[0]+1)
       # print(pos)
    print(pos)
