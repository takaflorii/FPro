def calc_triangular(n):
    triangular = 0
    for x in range(1, n + 1):
        triangular += x
    return triangular


def calc_factorial(n):
    factorial = 1
    for x in range(1, n + 1):
        factorial *= x
    return factorial


def reuse(number):
    total = 0
    for i in range(1, number + 1):
        if i % 2 == 1:
            total += calc_triangular(i)
        else:
            total += calc_factorial(i)
    return total