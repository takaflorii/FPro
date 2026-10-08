preco = int(input())
recebido = int(input())

troco = recebido - preco

notasde50 = troco // 50
troco = troco % 50

notasde20 = troco // 20
troco = troco % 20

notasde10 = troco // 10
troco = troco % 10

notasde5 = troco // 5

resultado = str(notasde50) + " " + str(notasde20) + " " + str(notasde10) + " " + str(notasde5)
print(resultado)