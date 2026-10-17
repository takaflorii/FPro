def greatest(num: int) -> int:
    digitos = []
    for d in str(num):
        digitos.append(int(d))

    digitos.sort(reverse=True)

    rayquaza = 0
    for d in digitos:
        rayquaza = rayquaza * 10 + d

    return rayquaza