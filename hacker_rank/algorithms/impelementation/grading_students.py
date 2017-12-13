def solve(grades):
    new_grades = []
    for grade in grades:
        if not grade < 38:
            threshold = ((grade // 5) + 1) * 5
            if threshold - grade < 3:
                new_grades.append(threshold)
                continue
        new_grades.append(grade)

    return new_grades


n = int(input().strip())
grades = []
grades_i = 0

for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)

result = solve(grades)

print("\n".join(map(str, result)))
