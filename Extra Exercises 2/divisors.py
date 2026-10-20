nani = int(input())
soma = 0
for i in range(1, nani + 1):
    if nani % i == 0:
        soma = soma + i
print(soma)