# You have isSubstring already.
# Given two strings, check if s2 is a rotation of s1 using only one isSubstring
# e.g. "waterbottle" is a rotation of "erbottlewat"


def is_rotation(string1, string2):
    if (len(string1) == len(string2)) and len(string2) > 0:
        double_string1 = string1 + string1
        return string2 in double_string1
    return False


print(is_rotation("waterbottle", "erbottlewat"))
