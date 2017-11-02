def is_number_palindrome(number):
    num = number
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10

    return rev == number


print(is_number_palindrome(123454321))
