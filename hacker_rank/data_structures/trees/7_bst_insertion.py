from common.BinarySearchTree import BinarySearchTree
from common.Tree import TreeNode


def insert(r: TreeNode, val):
    new_node = TreeNode(val)

    if not r:
        r = new_node
    else:
        if new_node.value <= r.value:
            if not r.left:
                r.left = new_node
            else:
                insert(r.left, new_node.value)
        else:
            if not r.right:
                r.right = new_node
            else:
                insert(r.right, new_node.value)

    return r


bst = BinarySearchTree(1)
insert(bst, 2)
insert(bst, 5)
insert(bst, 3)
insert(bst, 6)
result = insert(bst, 4)
print(result)
