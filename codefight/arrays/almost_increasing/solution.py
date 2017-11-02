def first_bad_pair(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return i
    return -1


def almost_increasing_sequence(sequence):
    first_bad_index = first_bad_pair(sequence)
    if first_bad_index == -1:
        return True
    if first_bad_pair(sequence[:first_bad_index] + sequence[first_bad_index + 1:]) == -1:
        return True
    if first_bad_pair(sequence[:first_bad_index + 1] + sequence[first_bad_index + 2:]) == -1:
        return True

    return False


print(almost_increasing_sequence([1, 3, 2, 1]))
print(almost_increasing_sequence([1, 3, 2]))
