direcoes = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
angulos = [0, 45, 90, 135, 180, 225, 270, 315]

def direcao_mais_proxima(angulo):
    if angulo >= 338:
        return "N"

    menor_diferenca = 360
    melhor_direcao = ""

    for i in range(len(angulos)):
        diferenca = abs(angulo - angulos[i])

        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            melhor_direcao = direcoes[i]
            
    return melhor_direcao

degree = int(input())
print(direcao_mais_proxima(degree))
