import math
angle = int(input())*math.pi/180  # convert to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)

velocidade = 18
temponoar = 2 * velocidade * sin_angle /10
distancia = velocidade * cos_angle * temponoar

print(round(distancia))