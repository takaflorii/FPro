dimensao = int(input())

linha = 0
if dimensao >= 3:
    while linha < dimensao:
        coluna = 0

        while coluna < dimensao:
            if dimensao % 2 != 0 and linha == dimensao // 2 and coluna == dimensao // 2:
                print("0", end="")
            elif dimensao % 2 == 0 and (linha == dimensao // 2 - 1 or linha == dimensao // 2) and (coluna == dimensao // 2 - 1 or coluna == dimensao // 2):
                print("0", end="")
            else:
                print("#", end="")

            coluna = coluna + 1

        print()
        linha = linha + 1

else:
    print("Dimensão inválida")