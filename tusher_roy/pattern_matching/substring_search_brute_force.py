def substring_search(input_string, pattern):
    for index_string in range(0, len(input_string) - len(pattern)):
        index_pattern = 0
        for index_pattern in range(0, len(pattern)):
            if input_string[index_string + index_pattern] != pattern[index_pattern]:
                break

        if index_pattern == len(pattern) - 1:
            return index_string

    return len(input_string)


print(substring_search("asdaxyzde", "xyz"))
