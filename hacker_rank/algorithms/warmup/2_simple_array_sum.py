def simple_array_sum(n, ar):
    sum = 0
    for item in ar:
        sum = sum + item

    return sum


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simple_array_sum(n, ar)
print(result)
