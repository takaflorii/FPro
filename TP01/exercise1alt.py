num = int(input("Introduz um número inteiro de 0 a 9: "))
result = num + num*11 + num*111

if num < 0 or num > 9:
    print("Número inválido. Por favor, introduza um número entre 0 e 9.")

else:
    print(f"O resultado da operação é: {result}")
