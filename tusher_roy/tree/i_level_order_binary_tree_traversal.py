from common.Queue import Queue
from common.Tree import TreeNode


def level_order_traversal(root: TreeNode):
    if not root:
        return None

    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        root = queue.dequeue()
        print(root.value)

        if root.left:
            queue.enqueue(root.left)

        if root.right:
            queue.enqueue(root.right)


# ex = TreeNode(4)
# bst_insert_iterative(ex, 3)
# bst_insert_iterative(ex, 10)
# bst_insert_iterative(ex, 7)
# bst_insert_iterative(ex, 5)
# bst_insert_iterative(ex, 2)
# level_order_traversal(ex)
