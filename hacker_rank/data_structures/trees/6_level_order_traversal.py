import sys

from common.BinarySearchTree import BinarySearchTree
from common.Queue import Queue


def level_order(root):
    if not root:
        return None

    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        val = queue.dequeue()
        sys.stdout.write(str(val.value) + " ")
        if val.left:
            queue.enqueue(val.left)
        if val.right:
            queue.enqueue(val.right)


bst = BinarySearchTree(1)
bst.add(2)
bst.add(5)
bst.add(3)
bst.add(6)
bst.add(4)
level_order(bst)
