# Algorithm Explanation: https://youtu.be/7uG0gLDbhsI?t=4m
from common.Queue import Queue

from common.Tree import TreeNode


def print_tree(root: TreeNode):
    if not root:
        return None

    queue = Queue()
    queue.enqueue(root)
    queue.enqueue(None)

    while not queue.is_empty() and queue.get_len() > 1:
        current = queue.dequeue()
        if current is None:
            queue.enqueue(None)
            print("\n")
            continue

        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)

        print(current.value, end=" ")


# tree = TreeNode(4)
# bst_insert_iterative(tree, 3)
# bst_insert_iterative(tree, 5)
# bst_insert_iterative(tree, 2)
# bst_insert_iterative(tree, 1)
# print_tree(tree)
