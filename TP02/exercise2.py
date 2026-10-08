hora = int(input())
minuto = int(input())

if hora < 0 or hora>=24 or minuto < 0 or minuto > 59:
    print("INVALID DATE FORMAT")

else:
    if hora < 12:
        periodo = "am"

    else:
        periodo = "pm"

    if hora > 12:
        hora =  hora - 12

    elif hora == 0:
        hora = 12

    if minuto == 0:
        print(hora, periodo)

    else:
        print(f'{hora}:{minuto:02d} {periodo}')