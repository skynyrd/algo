n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

primary_diagonal = 0
secondary_diagonal = 0

for i in range(0, n):
    primary_diagonal += a[i][i]

j = n - 1
i = 0

while j > -1 and i < n:
    secondary_diagonal += a[i][j]
    j += -1
    i += 1

print(abs(primary_diagonal - secondary_diagonal))

