n1 = int(input())
n2 = int(input())
result = 0

while n1 > 0 and n2 > 0:
    ult_digito1 = n1 % 10
    ult_digito2 = n2 % 10
    result = result * 100 + ult_digito1 * 10 + ult_digito2
    n1 = n1//10
    n2 = n2//10

print(result)