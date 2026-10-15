from math import factorial as fact

def fatorial(k):
    x = 0
    if k == 1:
        return 1
    else:
        m = k * fact(k-1)
        return m

n = 3
print(f"O fatorial de {n} é {fatorial(n)}")
