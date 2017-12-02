from common.Tree import TreeNode


def lca(node: TreeNode, value1, value2):
    if node.value > max(value1, value2):
        return lca(node.left, value1, value2)
    elif node.value < min(value1, value2):
        return lca(node.right, value1, value2)
    else:
        return node
