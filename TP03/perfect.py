def is_perfect(n):
    soma = 0
    for i in range(1, n):
        if n%i == 0:
            soma = soma + i
    if soma == n:
        return True
    else:
        return False