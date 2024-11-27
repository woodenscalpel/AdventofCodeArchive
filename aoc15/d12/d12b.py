import json
injson = open("input.txt","r").read()[:-1]
jstring = json.loads(injson)

def traverse(js):
    if type(js) is int:
        return js
    elif type(js) is str:
        return 0
    elif type(js) is dict:
        acc = 0
        red = False
        for x in js:
            acc += traverse(js[x])
            if js[x] == "red":
                red = True
        if red : return 0
        return acc
    else:
        acc = 0
        for x in js:
            acc += traverse(x)
        return acc

print(traverse(jstring))
