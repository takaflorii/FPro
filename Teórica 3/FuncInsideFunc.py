def funcao_interna(x):
    print("Funçao Interna")
    print(f"Número {x}")

def funcao_externa():
    print("Chamada antes da primeira interna")
    funcao_interna(1)
    print("Chamada antes da segunda interna")
    funcao_interna(2)

funcao_externa()