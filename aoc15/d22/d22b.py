import copy
mana = 500
hp = 50

bdmg = 9
bhp = 58 # 58

spellcosts = [53,73,113,173,229] #Missle,Drain,Shield,Poison,Recharge

startstate = {}
startstate["hp"] = 50
startstate["mana"] = 500
startstate["bhp"] = 58
startstate["armor"] = 0
startstate["pt"] = 0
startstate["st"] = 0
startstate["rt"] = 0
startstate["spent"] = 0
startstate["win"] = None

winningmana = [9999]

def tickeffects(state):
    if state["st"] > 0:
        state["armor"] = 7
        state["st"] -= 1
    else:
        state["armor"] = 0

    if state["pt"] > 0:
        state["pt"] -= 1
        state["bhp"] -= 3
        if state["bhp"] <= 0:
            state["win"] = True
            #print(state)
            winningmana.append(state["spent"])
    if state["rt"] > 0:
        state["rt"] -= 1
        state["mana"] += 101

def tickstate(oldstate):
    newstates = []

    oldstate["hp"] -= 1
    if oldstate["hp"] < 1:
        return []

    tickeffects(oldstate)
    
    if oldstate["win"] != None:
        return []
    
    if oldstate["mana"] < 53:
        oldstate["win"] = False
        return []

    for idx,cost in enumerate(spellcosts):
        state = oldstate.copy()

        state["mana"] -= cost
        state["spent"] += cost

        if idx == 0:
            state["bhp"] -= 4
            if state["bhp"] <= 0:
                state["win"] = True
                winningmana.append(state["spent"])

        if idx == 1:
            state["hp"] += 2
            state["bhp"] -= 2
            if state["bhp"] <= 0:
                state["win"] = True
                winningmana.append(state["spent"])

        if idx == 2:
            if state["st"] > 0:
                continue
            state["st"] = 6

        if idx == 3:
            if state["pt"] > 0:
                continue
            state["pt"] = 6

        if idx == 4:
            if state["rt"] > 0:
                continue
            state["rt"] = 5

        tickeffects(state)
        if state["win"] != None:
            continue

        state["hp"] -= bdmg - state["armor"]
        if state["hp"] < 1:
            continue
        newstates.append(state)
    return newstates

print(tickstate(startstate))

activestates = [startstate]

while activestates:
    newstates = []
    for s in activestates:
        newstates.extend(tickstate(s))
    print(min(winningmana))
    activestates = newstates

        



    
