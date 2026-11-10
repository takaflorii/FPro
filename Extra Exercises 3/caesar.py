import math

def fibonacci(n):
    sqrt_5 = math.sqrt(5)
    f_n = ((1 + sqrt_5)**n - (1 - sqrt_5)**n) / ((2**n) * sqrt_5)
    return round(f_n)

def caesar(message):
    resultado = ""
    n = 0
    
    for char in message:
        if "A" <= char <= "Z":
            shift = fibonacci(n)
            posicao_atual = ord(char) - ord("A")
            nova_posicao = (posicao_atual - shift) % 26
            nova_letra = chr(ord("A") + nova_posicao)
            resultado = resultado + nova_letra
            n = n + 1
        else:
            resultado = resultado + char
            
    return resultado