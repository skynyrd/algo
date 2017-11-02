# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3

import sys


def make_array_consecutive_2(statues):
    min = sys.maxsize
    max = -1
    for number in statues:
        if number > max:
            max = number
        if number < min:
            min = number

    totalDif = max - min + 1
    totalDif = totalDif - len(statues)
    return totalDif