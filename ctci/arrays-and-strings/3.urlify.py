# Replace all spaces with %20. String has sufficient space at the end to hold the additional characters, and 'true'
# length of string is given.
# at the end of the true string, there are whitespacecount in truestring * 2 whitespaces.

# input  "Mr John Smith    "
# output "Mr%20John%20Smith"


def replace_spaces(input_string, true_length):
    input_array = list(input_string)
    index = len(input_array) - 1

    if len(input_array) < true_length:
        input_array[true_length] = '\0'

    reverse_index = true_length - 1

    while reverse_index >= 0:
        if input_array[reverse_index] != ' ':
            input_array[index] = input_array[reverse_index]
            index -= 1
        else:
            input_array[index] = "0"
            input_array[index - 1] = "2"
            input_array[index - 2] = "%"
            index -= 3

        reverse_index -= 1

    return ''.join(input_array)


print(replace_spaces("asddsa qweq vv bt      ", 17))
