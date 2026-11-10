def collatz(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = int(n/2)
            sequence.append(n)
        else:
            n = int(n*3 + 1)
            sequence.append(n)
    result = str(sequence)

    return(result).strip("[]").replace(" ","")
