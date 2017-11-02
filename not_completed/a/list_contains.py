# The first coding question was to determine whether a list of integers with size N, contains all the numbers from
# one to N.


def contains_all_numbers(array):
    sum = 0
    array_length = len(array)
    for i in range(0, array_length):
        sum += array[i]

    if sum == array_length * (array_length + 1) / 2:
        print("GOOD")
    else:
        print("BAD")


contains_all_numbers([1,1,4])

'''
The answer provided by DG is awful.
For instance:a[1,1,4] would be given as true.

The answer is easier if you think of it in the opposite fashion. If it does not then there must be a duplicate 
or a number greater than or less than N. This is very easy to check for in O(n) time.
'''