# https://www.hackerrank.com/challenges/2d-array/problem

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

sumTop = 0
sumMiddle = 0
sumBottom = 0
max = -sys.maxsize

for row in range(0, 4):
    for col in range(0, 4):
        sumTop = sumTop + arr[row][col] + arr[row][col + 1] + arr[row][col + 2]
        sumMiddle = sumMiddle + arr[row + 1][col + 1]
        sumBottom = sumBottom + arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
        total = sumTop + sumMiddle + sumBottom
        max = total if total > max else max
        sumTop = 0
        sumMiddle = 0
        sumBottom = 0

print(max)
