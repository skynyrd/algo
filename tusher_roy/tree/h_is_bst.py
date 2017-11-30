from common.Tree import TreeNode


def is_bst(node: TreeNode, min, max):
    if not node:
        return True
    else:
        if min < node.value < max:
            return is_bst(node.left, min, node.value) and is_bst(node.right, node.value, max)
        else:
            return False
