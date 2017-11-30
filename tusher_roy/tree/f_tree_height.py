from common.Tree import TreeNode


def tree_height(root: TreeNode):
    if not root:
        return 0

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return 1 + max(left_height, right_height)

# Time and space complexity: O(n)
