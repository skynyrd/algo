from common.Tree import TreeNode


def in_order(node: TreeNode):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)
