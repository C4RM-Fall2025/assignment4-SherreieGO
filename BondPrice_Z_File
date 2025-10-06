def getBondPrice_Z(face, couponRate, times, yc):
    C = face * couponRate
    bondPrice = 0

    for t, y in zip(times, yc):
        if t == times [-1]:
            pv = (C +face) / (1 + y) ** t 
        else:
            pv = C / (1 + y) ** t 
        bondPrice = bondPrice + pv 
    
    return bondPrice
