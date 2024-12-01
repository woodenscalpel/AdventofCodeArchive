inp = open("input.txt","r").read().strip()
#inp = "A(1x5)BC"
#inp = "(3x3)ABC"
#inp = "A(2x2)BCD(2x2)EFG"
#inp = "X(8x2)(3x3)ABCY"
print(inp)
print(inp[0])

pointer = 0
newstring = ""

while pointer < len(inp):
    char = inp[pointer]
    if char == "(":
        inst = ""
        pointer += 1
        char = inp[pointer]
        while char != ")":
            pointer += 1
            inst += char
            char = inp[pointer]
        rn = inst.split("x")
        pointer += 1
        char = inp[pointer]
        newstring += inp[pointer:pointer+int(rn[0])]*int(rn[1])
        pointer += int(rn[0])
        pass
    else:
        newstring += char
        pointer += 1
print(newstring)
print(len(newstring))
