nani = int(input())

for j in range (1, nani + 1):
        espaços = " " * (nani - j)
        blocos = "#" * j
        divisao = "  "
        print(espaços + blocos + divisao + blocos)