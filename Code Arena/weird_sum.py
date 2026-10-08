a = int(input())
b = int(input())
soma = a + b
diferenca = a - b
produto = a * b

dif_par = int(diferenca % 2 == 0)
dif_impar = 1 - dif_par

resultado = dif_par * (2 * soma) + dif_impar * (soma + produto)
print(resultado)