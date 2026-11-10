def mult_every3rd(s):
    multiplicadores = []
    mult = 1
    nova_s = s[::3]
    for i in range(0, len(nova_s)):
        if nova_s[i].isdigit():
            multiplicadores.append(nova_s[i])
        else:
            multiplicadores.append(1)
    for num in multiplicadores:
        mult *= int(num)

    return mult

print(mult_every3rd("abcdef"))

