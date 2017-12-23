def check_palindrome(input_string):
    threshold = len(input_string) // 2

    for i in range(0, threshold):
        if input_string[i] != input_string[-i-1]:
            return False

    return True


print(check_palindrome("aaaabbaaaa"))
