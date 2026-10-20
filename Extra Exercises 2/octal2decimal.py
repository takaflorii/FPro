octal = input().strip()

if not all(d in "01234567" for d in octal):
    print("Not a valid number.")
else:
    result = 0
    for i in range(len(octal)):
        conversao = int(octal[i]) * (8 ** (len(octal) - 1 - i))
        result = result + conversao
    print(result)