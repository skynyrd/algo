def gcd_naive(a, b):
    best = 0
    for i in range(1, max(a, b)):
        if a % i == 0 and b % i == 0:
            best = i

    return best


print(gcd_naive(5, 15))
