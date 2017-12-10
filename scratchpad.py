# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

import sys

def test(arr):
    max = -sys.maxsize

    for i in range(0, len(arr)):
        if i + 1 != len(arr):
            product = arr[i] * arr[i+1]
            if product > max:
                max = product

    print(max)

test([3, 6, -2, -5, 7, 3])