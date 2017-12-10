def is_permutation(string1, string2):
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    if not len(string1) == len(string2):
        return False

    hash_map = {}

    for char in string1:
        if not hash_map.get(char, None):
            hash_map[char] = 1
        else:
            hash_map[char] += 1

    for char in string2:
        if not hash_map.get(char, None):
            return False
        else:
            hash_map[char] -= 1
            if hash_map[char] < 0:
                return False
    return True