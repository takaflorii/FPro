def fatorial(k):
    if k == 1:
        return 1
    else:
        while k > 1:
            m = k * fatorial(k-1)
            return m

n = 5
print(f"O fatorial de {n} é {fatorial(n)} ")