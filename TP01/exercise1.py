num = (input("Introduza um número inteiro de 0 a 9: "))
result = int(num) + int(num * 2) + int(num * 3)

if int(num) < 0 or int(num) > 9:
    print("Número inválido. Por favor, introduza um número entre 0 e 9.")
else:
    print(result)