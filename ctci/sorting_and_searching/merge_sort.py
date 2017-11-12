def merge(left, right):
    result = []
    cursor_left, cursor_right = 0, 0
    while cursor_left < len(left) and cursor_right < len(right):
        if left[cursor_left] < right[cursor_right]:
            result.append(left[cursor_left])
            cursor_left += 1
        else:
            result.append(right[cursor_right])
            cursor_right += 1

    while cursor_left < len(left):
        result.append(left[cursor_left])
        cursor_left += 1
    while cursor_right < len(right):
        result.append(right[cursor_right])
        cursor_right += 1

    return result


def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


print(merge_sort([1, 22, 0, 34]))
