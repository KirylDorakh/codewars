def high_and_low(numbers):
    numbers = sorted([int(i) for i in numbers.split()])
    return f'{numbers[-1]} {numbers[0]}'


print(high_and_low("1 2 -3 4 5"))


def high_and_low1(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
