# aaabbcdddeeeee -> a3b2c1d3e5
# if compressed one is longer than original string, return the original.


def compress(input_string):
    result = []
    count = 0

    for i in range(0, len(input_string)):
        count += 1
        if i + 1 >= len(input_string) or input_string[i] != input_string[i + 1]:
            result.append(input_string[i])
            result.append(str(count))
            count = 0

    return input_string if len(input_string) < len(result) else ''.join(result)


print(compress("abcccddeeee"))
