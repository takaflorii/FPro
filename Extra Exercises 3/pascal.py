import math

def pascal(n):
    resultado = ""
    for i in range(n):
        linha = ""

        for j in range(i + 1):

            valor = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
            linha = linha + str(valor) + " "
            
        resultado = resultado + linha.strip() + "\n"
        
    return resultado
