# https://www.hackerrank.com/challenges/reduced-string/problem

import sys


def super_reduced_string(input_string):
    result = ''

    for char in input_string:
        if result[-1:] == char:
            result = result[:-1]
        else:
            result += char

    return result if len(result) > 0 else "Empty String"


print(super_reduced_string("aaabbccc"))