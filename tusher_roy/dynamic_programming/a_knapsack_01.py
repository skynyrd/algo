# Explanation: https://youtu.be/8LusJS5-AGo


def knapsack_01(values, weights, total):
    total_items = len(weights)

    rows = total_items + 1
    cols = total + 1

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if j < weights[i - 1]:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j],
                                            values[i - 1] + matrix[i - 1][j - weights[i - 1]])

    return matrix[rows - 1][cols - 1]


if __name__ == '__main__':
    total_weight = 7
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    print(knapsack_01(values, weights, total_weight))
