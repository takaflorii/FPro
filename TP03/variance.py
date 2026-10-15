def avg_numbers(number):
    soma = 0
    media = 0
    for i in range(1, number + 1):
        soma = soma + i
    media = soma / number
    return media


def var_numbers(number, precision = 2):
    diferenca = 0
    sumatorio = 0
    for i in range(1, number+1):
        diferenca = i - avg_numbers(number)
        quadrado = diferenca ** 2
        sumatorio = sumatorio + quadrado

    variance = (sumatorio/number)
    return round(variance, precision)

