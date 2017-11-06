#          1
#        1   1
#      1   2   1
#     1  3   3   1
#   1  4   6   4   1


def pascal_triangle(col, row):
    if col == 0 or col == row or row == 0:
        return 1
    else:
        return pascal_triangle(col - 1, row - 1) + pascal_triangle(col, row - 1)


print(pascal_triangle(1, 4))
