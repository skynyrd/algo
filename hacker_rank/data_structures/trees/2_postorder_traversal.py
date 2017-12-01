from common.Tree import TreeNode


def post_order(node: TreeNode):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)
