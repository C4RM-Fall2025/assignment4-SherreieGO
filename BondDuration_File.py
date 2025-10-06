def getBondDuration (y, face, couponRate, m, ppy=1):
    C = face * couponRate / ppy
    N = int(m * ppy)

    price = 0
    weighted_sum = 0

    for t in range(1, N+1):
        discount = (1 + y / ppy) ** t
        pv_coupon = C / discount
        price = price + pv_coupon
        weighted_sum = weighted_sum + (t / ppy) * pv_coupon
    
    discount_face = (1 + y / ppy) ** N
    pv_face = face / discount_face
    price = price + pv_face
    weighted_sum = weighted_sum + (N / ppy) * pv_face

    duration = weighted_sum / price

    return duration
