import hashlib
start = 'ffykfhsq'
#start = 'abc'
print(hashlib.md5('abc'.encode('utf-8')).hexdigest())

ans = ""
n = 0
for digit in range(8):
    found = False
    while not found:
        n +=1
        teststring = start + str(n)
        md5s = hashlib.md5(teststring.encode('utf-8')).hexdigest()
        #print(md5s[:5])
        if(str(md5s[:5]) == "00000"):
            print(md5s)
            print(md5s[5])
            ans += str(md5s[5])
            found = True
print(ans)


