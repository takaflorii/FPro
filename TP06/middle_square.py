def next_middle_square(number, digits):
    k = digits // 2
    square = number * number
    middle = (square // (10**k)) % (10**digits)
    return middle


def cycle_length(number, digits):
    seen = set()

    while number not in seen:
        seen.add(number)
        number = next_middle_square(number, digits)

    target = number
    length = 1
    number = next_middle_square(number, digits)

    while number != target:
        number = next_middle_square(number, digits)
        length += 1

    return length