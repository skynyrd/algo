# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

#    1 2 3    1 0 3
#    4 0 5    0 0 0
#    3 3 3    3 0 0


def set_zeros(matrix):
    row_zeros = [False] * len(matrix)
    column_zeros = [False] * len(matrix[0])

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                row_zeros[i] = True
                column_zeros[j] = True

    for i in range(0, len(row_zeros)):
        if row_zeros[i]:
            for j in range(0, len(matrix[0])):
                matrix[i][j] = 0

    for i in range(0, len(column_zeros)):
        if column_zeros[i]:
            for j in range(0, len(matrix)):
                matrix[j][i] = 0


matrix = [[1, 2, 3], [4, 0, 5], [3, 3, 3]]
set_zeros(matrix)
print(matrix)
