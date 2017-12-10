def calculate_z(new_string):
    z_arr = [0] * len(new_string)

    left, right = 0, 0


def match_pattern(input_string, pattern):
    new_string = pattern + "$" + input_string

    z_array = calculate_z(new_string)

    result = []
    for i in range(0, len(z_array)):
        if z_array[i] == len(pattern):
            result.append(i - len(pattern) - 1)

    return result
