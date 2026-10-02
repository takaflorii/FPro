num = int(input("Introduz um número de 4 dígitos: "))
if num < 1000 or num > 9999:
    print("Número inválido. Por favor, introduza um número de 4 dígitos.")
else:
    print((num//1000)*1000,"\n",(num//100%10)*100,"\n",(num//10%10)*10,"\n",(num%10), sep="")