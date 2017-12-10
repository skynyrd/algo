def check_permutation_group(word_list):
    result = {}

    for word in word_list:
        word = word.replace(" ", "")

        hash_arr_for_word = [0] * 128  # assuming standard ascii

        for char in word:
            char_int = ord(char)
            hash_arr_for_word[char_int] += 1

        hash_for_word = ''.join(str(item) for item in hash_arr_for_word)

        if not result.get(hash_for_word, None):
            result[str(hash_for_word)] = [word]
        else:
            result[str(hash_for_word)] += [word]

    return list(result.values())


print(check_permutation_group([
    "pear",
    "amleth",
    "dormitory",
    "tinsel",
    "dirty room",
    "hamlet",
    "listen",
    "silnet",
]))
