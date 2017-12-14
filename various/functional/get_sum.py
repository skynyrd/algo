from typing import List


def get_sum(l: List[int]):
    return 0 if len(l) == 0 else l[0] + get_sum(l[1:])


print(get_sum([1, 2, 3]))
print(get_sum([1, 2, 3, 60]))
