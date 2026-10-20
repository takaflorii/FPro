nani = int(input())
result = 1+2 < 5
print(result)
if nani == 0:
    print(0)
else:
    for k in range(1, nani + 2):
        if k * k > nani:
            print(k - 1)
            break