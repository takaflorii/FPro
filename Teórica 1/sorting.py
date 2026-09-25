def ordenar_sequencia(sequencia):
    n = len(sequencia)
    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if sequencia[j] < sequencia[menor]:
                menor = j

        # troca os valores de posição
        sequencia[i], sequencia[menor] = sequencia[menor], sequencia[i]
    return sequencia


sequencia = input("Digite uma sequência de números separados por vírgula: ").split(",")
print("Sequência original:", sequencia)
print("Sequência ordenada:", ordenar_sequencia(sequencia))
