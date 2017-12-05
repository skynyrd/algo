def add_points(a, b, group_a, group_b):
    if a > b:
        group_a = group_a + 1
    elif a < b:
        group_b = group_b + 1

    return group_a, group_b


def solve(a0, a1, a2, b0, b1, b2):
    group_a, group_b = 0, 0

    group_a, group_b = add_points(a0, b0, group_a, group_b)
    group_a, group_b = add_points(a1, b1, group_a, group_b)
    group_a, group_b = add_points(a2, b2, group_a, group_b)

    return [group_a, group_b]


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))
