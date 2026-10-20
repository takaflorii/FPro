from math import pi
diametro = int(input())
preco = float(input())

area = pi * (diametro/2)**2

preco_por_cm = (preco*100) / area 

print(round(preco_por_cm,2))