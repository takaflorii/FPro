def alfabeto(n: int) -> str:
    todas_as_letras = "abcdefghijklmnopqrstuvwxyz"
    return todas_as_letras[:n]

def rangoli(n: int) -> str:
    unown = alfabeto(n)
    largura= 4 * n - 3 #Para N=3: temos 2(3)−1=5 letras (c, b, a, b, c) e como temos (2N−1) letras, o número de hífenes é: (2N−1)−1=2N−2. Logo a largura total da linha é: 2N−1 + 2N−2 = 4N−3.
    linhas = []
    
    for i in range(n):
        letras_na_linha = unown[n - 1 - i : n]

        canhoto = letras_na_linha[::-1]
        direitinho = letras_na_linha[1:]
        
        linha_com_hifen = "-".join(canhoto + direitinho)
        linhas.append(linha_com_hifen.center(largura, "-"))
    

    padrao_completo = linhas + linhas[:-1][::-1]

    return "\n".join(padrao_completo)