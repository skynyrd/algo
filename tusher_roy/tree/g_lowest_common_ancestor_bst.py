# explanation: https://youtu.be/TIoCCStdiFo
from common.Tree import TreeNode


def lca_bst(root: TreeNode, node1: TreeNode, node2: TreeNode):
    if root.value > max(node1.value, node2.value):
        return lca_bst(root.left, node1, node2)
    elif root.value < min(node1.value, node2.value):
        return lca_bst(root.right, node1, node2)
    else:
        return root
