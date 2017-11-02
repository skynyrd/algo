# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data
# structures? Ask if the input string is ASCII or a Unicode. Assuming its standard ASCII:


# O(n) solution, can be discussed that its O(1) as loop will never iterate more than 128 chars. Space = O(c)
def is_unique_chars(input_string):
    if len(input_string) > 128:
        return False

    char_exist_map = [None] * 128
    for char in input_string:
        char_as_int = ord(char)

        if char_exist_map[char_as_int]:
            return False

        char_exist_map[char_as_int] = True

    return True


print(is_unique_chars("deneme"))
print(is_unique_chars("abcksoqp"))
