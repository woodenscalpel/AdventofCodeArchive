#start = "hepxcrrq"
start = "hepxxyzz"
start = [ord(x) for x in start]

Aidx = ord('a')
Zidx = ord('z')

print(start)

def increment(old):
    old[-1] +=1
    for i in range(1,8):
        if old[-i] > Zidx:
            old[-i] = Aidx
            old[-i-1] +=1
    return old

def passcheck(password):
    if ord('i') in password or ord('o') in password or ord('l') in password:
        return False

    #straight
    straight = False
    for i in range(6):
        if password[i+1] == password[i] +1 and password[i+2] == password[i+1] +1:
            straight = True

    #pairs
    pairs = False
    for x in range(7):
        if password[x+1] == password[x]:
            for y in range(7):
                if password[y+1] == password[y]:
                    if x != y and x != y+1 and x != y-1:
                        pairs = True
    return straight and pairs

valid = False

while not valid:
    start = increment(start)
    valid = passcheck(start)

print([chr(s) for s in start])
