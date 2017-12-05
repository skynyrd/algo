n = int(input().strip())
temp = n
s = 0

while n > -1 and s <= temp:
    if s > 0:
        for i in range(0, n):
            print(" ", end="")
        for j in range(0, s):
            print("#", end="")
        print("")
    n -= 1
    s += 1
