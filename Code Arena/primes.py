minimo = int(input())
maximo = int(input())

primos = ""

for num in range(minimo, maximo + 1):
    if num > 1:
        num_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                num_primo = False
                break
        if num_primo:
            primos = primos + str(num) + " "

print("Prime numbers between " + str(minimo) + " and " + str(maximo) + " are: " + primos)