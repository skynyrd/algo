from common.Tree import TreeNode


def pre_order(node: TreeNode):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


def in_order(node: TreeNode):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


def post_order(node: TreeNode):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


# Time Complexity O(n) because we visit every node.
# Size of the stack in the worst case is height of the binary tree.

