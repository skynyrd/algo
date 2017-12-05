def a_very_big_sum(n, ar):
    sum = 0
    for item in ar:
        sum = sum + item
    return sum

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = a_very_big_sum(n, ar)
print(result)