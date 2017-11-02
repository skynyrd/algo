import sys


def make_array_consecutive(statues):
    min_number = sys.maxsize
    max_number = -sys.maxsize

    for number in statues:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number

    consecutive_size = max_number - min_number + 1
    return consecutive_size - len(statues)


print(make_array_consecutive([6, 2, 3, 8]))
