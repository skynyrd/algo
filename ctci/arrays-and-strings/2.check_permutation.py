# Given two strings, write a method to decide if one is a permutation of the other
# input ABC, BAC = true, input ABC, DAB = false
# Ask that the comparison is case sensitive or not, also ask whitespace is significant or not


def check_permutation_high_level(string1, string2):
    if len(string1) != len(string2):
        return False
    return ''.join(sorted(string1)) == ''.join(sorted(string2))


print(check_permutation_high_level("ABC", "CAB"))


def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    letters = [0] * 128  # assuming standard ASCII

    for char in string1:
        char_as_int = ord(char)
        letters[char_as_int] += 1

    for char in string2:
        char_as_int = ord(char)
        letters[char_as_int] -= 1

        if letters[char_as_int] < 0:
            return False

    return True


print(check_permutation("A C", "CA "))
