import sys

arr = list(map(int, input().strip().split(' ')))

maximum, minimum = -sys.maxsize, sys.maxsize

for i in range(0, len(arr)):
    sum = 0
    for j in range(0, len(arr)):
        if i != j:
            sum += arr[j]
    if sum > maximum:
        maximum = sum
    if sum < minimum:
        minimum = sum

print(minimum, maximum)