# Check if the input string is a permutation of a palindrome.
# input: Tact Coa
# output: True (taco cat, or atco cta")

# SOLUTION O(N)


def get_rounded_value(char):
    int_z = ord("z")
    int_a = ord("a")
    int_Z = ord("Z")
    int_A = ord("A")
    int_char = ord(char)

    if int_z >= int_char >= int_a:
        return int_char - int_a
    if int_Z >= int_char >= int_A:
        return int_char - int_A
    return -1


def build_char_freq_table(input_string):
    char_freq_table = [0] * (ord("z") - ord("a") + 1)

    for char in input_string:
        rounded_value = get_rounded_value(char)
        if rounded_value != -1:
            char_freq_table[rounded_value] += 1

    return char_freq_table


def is_permutation_of_palindrome(input_string):
    table = build_char_freq_table(input_string)
    found_odd = False

    for count in table:
        if count % 2 == 1:
            if found_odd:
                return False
            found_odd = True

    return True


print(is_permutation_of_palindrome("Tact Coa"))

# Alternative approach:

def perpalindrome(input_str):
    input_str = input_str.replace(" ", "")

    char_freq = {}
    for char in input_str:
        if not char_freq.get(char, None):
            char_freq[char] = 1
        else:
            char_freq[char] += 1

    odds = 0
    evens = 0

    for key in char_freq:
        if char_freq[key] % 2 == 0:
            evens += 1
        else:
            odds += 1

    if len(input_str) % 2 == 0:
        if odds > 0:
            return False
        else:
            return True
    else:
        if odds > 1:
            return False
        return True
