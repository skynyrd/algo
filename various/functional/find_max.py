from typing import List


# If there is single element, return it.
# Else return maximum of following.
#     a) Last Element
#     b) Value returned by recursive call
#        for n-1 elements.

def find_max(l: List[int]):
    def find_max_inner(l: List[int], list_length):
        if list_length == 1:
            return l[0]
        return max(l[list_length - 1], find_max_inner(l, list_length - 1))

    return find_max_inner(l, len(l))


print(find_max([1, 5, 3]))

# max(3, find_max_inner([1,5,3], 2))
# max(3, max(5, find_max_inner([1,5,3], 1)))
# max(3, max(5, 1))
# max(3, 5)
# 5

