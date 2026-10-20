a = int(input())
b = int(input())
c = int(input())

max_ab = a * (a >= b) + b * (b > a)
max_abc = max_ab * (max_ab >= c) + c * (c > max_ab)

print(max_abc)