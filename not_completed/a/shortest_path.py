# Given a matrix representing a gold field with holes, trees and steppable grass (value = 1, can step, 0 = hole,
# n > 1 = a tree of length n). You have to walk the field and chopping all the trees. Always starting with the shortest
# tree. Return the shortest number of steps in order to achieve this. (Starting from the top left corner of the field)


#   0  1  3  1
#   1  2  3  1
#   0  1  4  1
#   4  0  1  3

# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/