def is_number_palindrome(input_int):
    num = input_int
    rev = 0

    while num > 0:
        last = num % 10
        rev = rev * 10 + last
        num = num // 10

    return input_int == rev


print(is_number_palindrome(123454321))
