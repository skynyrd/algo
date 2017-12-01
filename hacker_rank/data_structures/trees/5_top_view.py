from common.BinarySearchTree import BinarySearchTree
from common.Tree import TreeNode
import sys


def top_view_rec(root: TreeNode, isLeft, result):
    if not root:
        return None

    if isLeft:
        top_view_rec(root.left, isLeft, result)
    else:
        top_view_rec(root.right, isLeft, result)

    result.append(root.value)


def top_view(root: TreeNode):
    left_elements = []
    right_elements = []

    top_view_rec(root, True, left_elements)
    top_view_rec(root, False, right_elements)

    result = left_elements[:-1] + [root.value] + right_elements[::-1][1:]

    for item in result:
        sys.stdout.write(str(item) + " ")


bst = BinarySearchTree(1)
bst.add(2)
bst.add(5)
bst.add(3)
bst.add(6)
bst.add(4)
top_view(bst)
