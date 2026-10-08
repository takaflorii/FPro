width = int(input())
height = int(input())
linha = 0

while linha < height:
    coluna = 0
    while coluna < width:
        print("#", end = "")
        coluna = coluna + 1

    print()
    linha = linha + 1
