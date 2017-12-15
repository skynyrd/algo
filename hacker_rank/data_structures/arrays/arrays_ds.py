# https://www.hackerrank.com/challenges/arrays-ds/problem

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

while n > 0:
    print(arr[n - 1], end=' ')
    n -= 1
