def adigits(a, b, c):
    if a <= b and a <= c:
        a = a*100
        if b <= c:
            b = b*10
            c = c
        else:
            c = c*10
            b = b
    elif b<= c and b <=a:
        b = b*100
        if a <= c:
            a = a*10
            c = c
        else:
            c = c*10
            a = a
    elif c<= a and c <= b:
        c = c*100
        if a <= b:
            a = a*10
            b = b
        else:
            b = b*10
            a = a

    return (a + b + c)
