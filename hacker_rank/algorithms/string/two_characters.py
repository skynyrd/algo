# https://www.hackerrank.com/challenges/two-characters/problem
# Algorithm explanation: https://www.hackerrank.com/challenges/two-characters/forum/comments/280681

input_str_len = int(input().strip())
input_str = input().strip()

distinct_str = sorted(set(input_str))

letter_matrix = [[None for _ in range(-1, len(distinct_str))] for _ in range(-1, len(distinct_str))]
count_matrix = [[0 for _ in range(-1, len(distinct_str))] for _ in range(-1, len(distinct_str))]

for i, char in enumerate(distinct_str):
    letter_matrix[0][i + 1] = char
    letter_matrix[i + 1][0] = char
    count_matrix[0][i + 1] = char
    count_matrix[i + 1][0] = char
    count_matrix[i][i] = -1

count_matrix[len(distinct_str)][len(distinct_str)] = -1

for char in input_str:
    char_index = letter_matrix[0].index(char)

    for i in range(1, len(letter_matrix)):
        if letter_matrix[i][char_index] == letter_matrix[i][0] or letter_matrix[i][char_index] is None:
            if count_matrix[i][char_index] != -1:
                count_matrix[i][char_index] += 1
        else:
            count_matrix[i][char_index] = -1

        if letter_matrix[char_index][i] == letter_matrix[0][i] or letter_matrix[i][char_index] is None:
            if count_matrix[char_index][i] != -1:
                count_matrix[char_index][i] += 1
        else:
            count_matrix[char_index][i] = -1

        letter_matrix[i][char_index] = char
        letter_matrix[char_index][i] = char


max_count = -1
letter_one, letter_two = None, None

for i in range(1, len(count_matrix)):
    for j in range(1, len(count_matrix[0])):
        if count_matrix[i][j] > max_count:
            max_count = count_matrix[i][j]
            letter_one = count_matrix[i][0]
            letter_two = count_matrix[0][j]

if max_count <= 0:
    print(0)
else:
    eliminated = input_str.replace(letter_one, "").replace(letter_two, "")
    print(len(input_str) - len(eliminated))
