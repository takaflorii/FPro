def dogs(h_age):
    d_age = 0
    for i in range(1, h_age+1):
        if h_age <= 2:
            d_age = i * 10.5
        
        if h_age > 2:
            d_age = 21 + (h_age-2) * 4
    return d_age