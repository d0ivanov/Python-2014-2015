import math


def sums_upto(number):
    member = 2**int(math.log(number, 2))
    if number - member > 0:
        return [member] + sums_upto(number - member)
    else:
        return [member]


def powers_of_two_remain(numbers):
    powers = [sums_upto(x) for x in numbers]
    flat = [item for sublist in powers for item in sublist]
    remaining = [x for x in flat if flat.count(x) % 2 != 0]
    return not not remaining
