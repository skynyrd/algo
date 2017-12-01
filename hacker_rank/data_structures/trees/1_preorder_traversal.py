from common.Tree import TreeNode


def pre_order(node: TreeNode):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)