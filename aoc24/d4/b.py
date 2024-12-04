f = open("input.txt","r").readlines()

parsed = []
for line in f:
    line = line.strip()
    parsed.append([x for x in line])
print(parsed)

print(len(parsed))
print(len(parsed[0]))



def left():
    acc = 0
    for row in range(len(parsed)):
        for col in range(len(parsed)-3):
            string = "".join(parsed[row][col:col+4])
            stringrev = "".join(reversed(parsed[row][col:col+4]))
            if string == "XMAS" or stringrev == "XMAS":
                acc += 1
    return acc

def up():
    acc = 0
    for row in range(len(parsed)-3):
        for col in range(len(parsed)):
            string = "".join([parsed[row][col]+parsed[row+1][col]+parsed[row+2][col]+parsed[row+3][col]])
            stringrev = "".join(reversed([parsed[row+3][col]+parsed[row+2][col]+parsed[row+1][col]+parsed[row+0][col]]))
            print(string,stringrev)
            if string == "XMAS" or stringrev == "XMAS":
                acc += 1
    return acc

def ru():
    acc = 0
    for row in range(len(parsed)-3):
        for col in range(len(parsed)-3):
            string = "".join([parsed[row][col]+parsed[row+1][col+1]+parsed[row+2][col+2]+parsed[row+3][col+3]])
            stringrev = "".join(reversed([parsed[row+3][col+3]+parsed[row+2][col+2]+parsed[row+1][col+1]+parsed[row+0][col]]))
            print(string,stringrev)
            if string == "XMAS" or stringrev == "XMAS":
                acc += 1
    return acc
 
def lu():
    acc = 0
    for row in range(len(parsed)-3):
        for col in range(len(parsed)-3):
            string = "".join([parsed[row+3][col]+parsed[row+2][col+1]+parsed[row+1][col+2]+parsed[row][col+3]])
            stringrev = "".join(reversed([parsed[row][col+3]+parsed[row+1][col+2]+parsed[row+2][col+1]+parsed[row+3][col]]))
            print(string,stringrev)
            if string == "XMAS" or stringrev == "XMAS":
                acc += 1
    return acc
 
def mtop():
    acc = 0
    for row in range(1,len(parsed)-1):
        for col in range(1,len(parsed)-1):
            if parsed[row][col] == "A":
                #MTOP
                if parsed[row-1][col+1] == "M" and parsed[row-1][col-1] == "M" and parsed[row+1][col-1] == "S" and parsed[row+1][col+1] == "S":
                    acc += 1
                #MBOT
                if parsed[row-1][col+1] == "S" and parsed[row-1][col-1] == "S" and parsed[row+1][col-1] == "M" and parsed[row+1][col+1] == "M":
                    acc += 1
                #MLEFT
                if parsed[row-1][col+1] == "S" and parsed[row-1][col-1] == "M" and parsed[row+1][col-1] == "M" and parsed[row+1][col+1] == "S":
                    acc += 1
                #MRIGHT
                if parsed[row-1][col+1] == "M" and parsed[row-1][col-1] == "S" and parsed[row+1][col-1] == "S" and parsed[row+1][col+1] == "M":
                    acc += 1
                
    return acc
 
                

acc = 0
acc += left()
print(acc)
acc += up()
print(acc)
acc += ru()
print(acc)
acc += lu()
print(acc)
acc = 0
acc += mtop()
print(acc)
