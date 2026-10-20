def persistence(n):
    pers_count = 0
    soma = 0
    while n >= 10:
        soma = 0
        while n > 0:
            digito = n % 10
            n = n // 10
            soma = soma + digito
        n = soma
        pers_count += 1
    return pers_count
