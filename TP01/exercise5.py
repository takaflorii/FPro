princAmount = int(input("Introduza o montante: "))
interesse = float(input("Introduza o interesse do juro: "))
freq = int(input("Qual a frequência que paga o juro no ano?: "))
t = 2
amount = princAmount*((1+(interesse/freq))**(freq*t))
print(round(amount,3))