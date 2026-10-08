import math
K = 50
constante = (2 * math.sqrt(2)) / 9801


soma = 0
for k in range(K + 1):
    numerador = math.factorial(4 * k) * (1103 + 26390 * k)
    denominador = (math.factorial(k) ** 4) * (396 ** (4 * k))
    soma = soma + numerador / denominador

pi = 1 / (constante * soma)

print(round(pi, 8))