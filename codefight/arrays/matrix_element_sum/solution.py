def matrix_element_sum(matrix):
    column_map = {}
    price = 0

    for row in matrix:
        for index, item in enumerate(row):
            if item == 0:
                column_map[str(index)] = False
            else:
                check_price = column_map.get(str(index), True)
                if check_price:
                    price += item

    return price


print(matrix_element_sum([[0, 1, 1, 2],
                          [0, 5, 0, 0],
                          [2, 0, 3, 3]]))
