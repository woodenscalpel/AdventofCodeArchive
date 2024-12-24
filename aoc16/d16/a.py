
def dragon(a):
    b = reversed(a)
    c = ""
    for char in b:
        if char == "0":
            c += "1"
        if char == "1":
            c += "0"
    return a + "0" + c

def checksum(data):
    p = 0
    newsum = ""
    while p < len(data):
        if data[p:p+2] == "00" or data[p:p+2] == "11":
            newsum += "1"
        else:
            newsum += "0"
        p += 2
    if len(newsum) % 2 == 0:
        return checksum(newsum)
    else:
        return newsum

data = "11101000110010100"
#targetlen = 272
targetlen = 35651584
while len(data) < targetlen:
    data = dragon(data)

checksumdata = data[:targetlen]
print(checksumdata)
#print(checksum("110010110100"))
print(checksum(checksumdata))

