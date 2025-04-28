from functools import reduce


def sum_numbers(numbers=None):
    if numbers is None:
        return reduce(lambda x,y: x+y, range(101))
    elif not numbers:
        return 0
    return reduce(lambda x,y: x+y, numbers)

print(sum_numbers([]))