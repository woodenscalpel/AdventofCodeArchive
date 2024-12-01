import hashlib
start = 'ffykfhsq'
#start = 'abc'
print(hashlib.md5('abc'.encode('utf-8')).hexdigest())

ans = ["?","?","?","?","?","?","?","?"]
n = 0
for digit in range(100):
    found = False
    while not found:
        n +=1
        teststring = start + str(n)
        md5s = hashlib.md5(teststring.encode('utf-8')).hexdigest()
        #print(md5s[:5])
        if(str(md5s[:5]) == "00000"):
            print(md5s)
            pos = md5s[5]
            char = md5s[6]
            #ans += str(md5s[5])
            try: 
                pos = int(pos)
                print(int(pos))
                if(int(pos) < 8):
                    if(ans[pos] == "?"):
                        ans[pos] = char
                        
                        print(ans)
                    #ans = ans[:pos] + char + ans[pos:]

                found = True
            except:
                pass
print(ans)


