def check_palindrome(input_str):
    threshold = len(input_str) // 2

    for i in range(0, threshold):
        if input_str[i] != input_str[-i-1]:
            return False

    return True