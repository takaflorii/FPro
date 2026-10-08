num = int(input())

for i in range(1, 11):
    res = num * i
    if i == num:
            break
    print(f"{num} x {i} = {res}")
   
if i == num:
      print(f"{num} ^ {2} = {num**2}")