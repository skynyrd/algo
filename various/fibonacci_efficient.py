def fibonacci_efficient(n):
    fib_array = [0] * n
    fib_array[0] = 0
    fib_array[1] = 1

    for i in range(2, n):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2]

    return fib_array[n - 1]


print(fibonacci_efficient(100))

# Analysis:
# T(n) = 2n + 2, so T(100) = 202 lines of execution..
