def change(amount):
    change = []
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    for i in coins:
        while amount >= i:
            amount -= i
            change.append(i)
    return change