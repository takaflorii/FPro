def is_looping_number(n):
    if n < 10:
        return True
    
    ultimo = n % 10
    n = n // 10
    
    while n > 0:
        anterior = n % 10
        diff = abs(ultimo - anterior)
        if diff != 1 and diff != 9:
            return False
        ultimo = anterior
        n = n // 10
        
    return True

n = int(input())

if is_looping_number(n):
    print("Looping number")
else:
    print("Not a looping number")