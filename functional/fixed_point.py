# Find x that f(x) is equal to x

from typing import Callable

tolerance = 0.0001


def is_close_enough(x, y):
    return abs(x - y) / x < tolerance


def fixed_point(func: Callable[[float], float], first_guess: float) -> float:
    def iterate(guess):
        nxt = func(guess)
        if is_close_enough(guess, nxt):
            return nxt
        else:
            return iterate(nxt)

    return iterate(first_guess)


print(fixed_point(lambda x: 1 + x / 2, 1))
