num = int(input())

reverso = 0

while num > 0:
    ult_digito = num % 10
    reverso = reverso * 10 + ult_digito
    num = num // 10

print(reverso)