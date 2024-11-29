dmg = 0
armor = 0
cost = 0

#cost, dmg,armor
weapons = [[8,4,0],[10,5,0],[25,6,0],[40,7,0],[74,8,0]]
armor = [[0,0,0],[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5]]
rings = [[0,0,0],[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]


def simulate(dmg,armor):
    b_hp = 104
    b_dmg = 8
    b_armor = 1

    hp = 100

    while True:

        b_hp -= (dmg - b_armor)
        if b_hp <= 0:
            return True
        hp -= (b_dmg - armor)
        if hp <= 0:
            return False


maxcost = 0

for w in weapons:
    for a in armor:
        for i1 in range(len(rings)):
            for i2 in range(len(rings)):
                r1 = rings[i1]
                if i1 != i2:
                    r2 = rings[i2]
                else:
                    r2 = [0,0,0]

                tcost = w[0] + a[0] + r1[0] + r2[0]
                dmg = w[1] + a[1] + r1[1] + r2[1]
                arm = w[2] + a[2] + r1[2] + r2[2]

                if not simulate(dmg,arm):
                    if tcost > maxcost:
                        maxcost = tcost
print(maxcost)
