from common.Tree import TreeNode


def tree_size(node: TreeNode):
    if not node:
        return 0

    left_size = tree_size(node.left)
    right_size = tree_size(node.right)

    return left_size + right_size + 1
