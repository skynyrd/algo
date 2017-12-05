def substring_search(input_string, search_string):
    search_index, input_index, cursor_for_input = 0, 0, 0

    while search_index < len(search_string) and input_index < len(input_string):
        if search_string[search_index] == input_string[cursor_for_input]:
            cursor_for_input += 1
            search_index += 1
            continue
        else:
            input_index += 1
            search_index = 0


print(substring_search("axyzde", "xsy"))
