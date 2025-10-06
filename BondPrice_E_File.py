def getBondPrice_E(face, couponRate, yc):
    C = face * couponRate
    bondPrice = 0
    
    for t, y in enumerate(yc, start =1):
        if t < len(yc):
            pv_coupon = C / (1 + y) **t
            bondPrice = bondPrice + pv_coupon
        else:
            pv_total = (C + face) / (1 + y) ** t 
            bondPrice = bondPrice + pv_total 
    return bondPrice
