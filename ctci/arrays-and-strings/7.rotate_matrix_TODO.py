# Rotate N * N matrix by 90 degree.

#   1 2 3       7 4 1
#   4 5 6       8 5 2
#   7 8 9       9 6 3


def rotate_matrix(matrix, n):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise Exception("Matrix is not in N * N format")

    for i in range(0, n):
        temp = matrix[i][i]

        matrix[i][i] = matrix[n - 1][i]
        matrix[n - 1][i] = matrix[n - 1][n - 1]
        matrix[n - 1][n - 1] = matrix[i][n - 1]
        matrix[i][n - 1] = temp

    return matrix


sample_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated_matrix = rotate_matrix(sample_matrix, 3)
print(rotated_matrix)
