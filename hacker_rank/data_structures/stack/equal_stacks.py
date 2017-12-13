n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
stack1 = [int(h1_temp) for h1_temp in input().strip().split(' ')][::-1]
stack2 = [int(h2_temp) for h2_temp in input().strip().split(' ')][::-1]
stack3 = [int(h3_temp) for h3_temp in input().strip().split(' ')][::-1]


def get_count(stack):
    count = 0
    for item in stack:
        count += item

    return count


c1 = get_count(stack1)
c2 = get_count(stack2)
c3 = get_count(stack3)

while c1 != c2 or c2 != c3:
    top_of_1 = stack1[-1:]
    top_of_2 = stack2[-1:]
    top_of_3 = stack3[-1:]

    if c1 >= c2:
        if c1 >= c3:
            tallest = stack1
            r = tallest.pop()
            c1 -= r
        else:
            tallest = stack3
            r = tallest.pop()
            c3 -= r
    else:
        if c2 >= c3:
            tallest = stack2
            r = tallest.pop()
            c2 -= r
        else:
            tallest = stack3
            r = tallest.pop()
            c3 -= r

print(c1)
