from common.Tree import TreeNode
from tusher_roy.tree.c_bst_insert_iterative import bst_insert_iterative


def level_order_traversal(root: TreeNode):
    if not root:
        return None

    queue = [root]

    while len(queue) > 0:
        root = queue.pop(0)
        print(root.value)

        if root.left:
            queue.append(root.left)

        if root.right:
            queue.append(root.right)


ex = TreeNode(4)
bst_insert_iterative(ex, 3)
bst_insert_iterative(ex, 10)
bst_insert_iterative(ex, 7)
bst_insert_iterative(ex, 5)
bst_insert_iterative(ex, 2)
level_order_traversal(ex)
