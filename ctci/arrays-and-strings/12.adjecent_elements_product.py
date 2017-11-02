# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

import sys


def adjacent_elements_product(input_array):
    arr_length = len(input_array)
    max = -sys.maxsize
    for i in range(arr_length):
        if (i + 1) < arr_length:
            pair_multiplication_result = input_array[i] * input_array[i + 1]
            if pair_multiplication_result > max:
                max = pair_multiplication_result

    return max
