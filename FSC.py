while True:
    a = str(input())
    if len(a) == 8:
        for index in range(len(a)):
            ch = a[index]
            if (ch != "0" and ch != "1"):
                print("Erro, apenas 0 e 1")
                break

        if (ch != "0" and ch != "1") is False:
            if a[1:4] == "000":
                if a[4:8] == "0000":
                    print("Zero")
                else:
                    print("Subnormal")


            elif a[1:4] == "111":
                if a[4:8] == "0000":
                    print("Infinito")
                else:
                    print("NaN")

            else:
                print("Normalizado")
    else:
        print("Introduza um número de 8 dígitos")



