# time complexity is O(n) for the worst case. (each node has only child, linear tree)
# if the tree is balanced, then the worst case time complexity is O(logn)
from common.Tree import TreeNode


#       10
#      /  \
#     /    \
#    -5    16
#   /  \     \
#  /    \     \
# -8     7    18

def bst_insert_iterative(root: TreeNode, data):
    node = TreeNode(data)
    if not root:
        return node

    parent, current = None, root

    while current is not None:
        parent = current
        if current.value <= data:
            current = current.right
        else:
            current = current.left

    if parent.value <= data:
        parent.right = node
    else:
        parent.left = node

    return node

# Complexity: O(logn)

# root = TreeNode(5)
# bst_insert_iterative(root, 3)
# bst_insert_iterative(root, 1)
# bst_insert_iterative(root, 2)
# bst_insert_iterative(root, 4)
# pass
