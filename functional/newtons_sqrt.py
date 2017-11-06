def sqrt(number):
    def is_good_enough(guess):
        return abs(guess * guess - number) / number < 0.01

    def improve(guess):
        return (guess + number / guess) / 2

    def sqrt_iter(guess):
        if is_good_enough(guess):
            return guess
        else:
            return sqrt_iter(improve(guess))

    return sqrt_iter(1)


print(sqrt(1600))
