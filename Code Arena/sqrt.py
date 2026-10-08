n = float(input())

a = 0.0
if n < 1:
    b = 1.0
else:
    b = n

while True:
    
    medio = (a + b) / 2
    
    if medio * medio == n or round(a, 5) == round(b, 5):
        break
        
    if medio * medio > n:
        b = medio
    else:
        a = medio

print(round(medio, 5))