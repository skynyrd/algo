# Given two strings, write a function to check if they are one edit (or zero edits) away.
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false


def one_edit_replace(input1, input2) -> bool:
    i = 0
    one_edit = False

    while i < len(input2):
        if input1[i] != input2[i]:
            if one_edit:
                return False
            one_edit = True
        i += 1

    return True


def one_edit_insert(short_input, long_input) -> bool:
    short_index = 0
    long_index = 0

    while short_index < len(short_input) and long_index < len(long_input):
        if short_input[short_index] == long_input[long_index]:
            short_index += 1
            long_index += 1
        else:
            if short_index == long_index:
                long_index += 1
                continue
            return False

    return True


def one_edit_away(input1, input2):
    if len(input1) == len(input2):
        return one_edit_replace(input1, input2)
    elif len(input1) + 1 == len(input2):
        return one_edit_insert(input1, input2)
    elif len(input1) - 1 == len(input2):
        return one_edit_insert(input2, input1)
    else:
        return False


print(one_edit_away("pale", "ple"))
print(one_edit_away("pales", "pale"))
print(one_edit_away("pale", "bale"))
print(one_edit_away("pale", "bae"))
print(one_edit_away("pale", "pal"))
