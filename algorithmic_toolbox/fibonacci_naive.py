def fibonacci_naive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


print(fibonacci_naive(30))

# Analysis:
#
# Too slow algorithm.
#
# if n <= 2, 2 lines of code.
# else, T(n-1) + T(n-2) + 3 lines of code.
#
# T(n) >= F(n)
# T(100) ~ 1.77 . 10^21 ~ 56000 Years at 1 GHz
