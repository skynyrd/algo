# Write a function to validate a binary search tree.
# Assume there are supporting classes and functions already.
# Try to prioritise speed - don't worry too much about memory.
# What other test cases would you use?
# How to do it without recursion? TODO


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_valid_bst(root_node):
    return is_valid_rec(root_node, float("-inf"), float("inf"))


def is_valid_rec(root_node, low, high):
    if root_node is None:
        return True

    return low < root_node.val < high \
           and is_valid_rec(root_node.left, low, root_node.val) \
           and is_valid_rec(root_node.right, root_node.val, high)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(is_valid_bst(root))
