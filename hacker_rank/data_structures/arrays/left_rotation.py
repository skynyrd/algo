# https://www.hackerrank.com/challenges/array-left-rotation/problem


def left_rotation(x, d):
    d = d % len(x)
    return x[d:] + x[:d]


if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = left_rotation(a, d)
    print(" ".join(map(str, result)))
