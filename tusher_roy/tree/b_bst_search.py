from common.Tree import TreeNode


def bst_search(root: TreeNode, key):
    if not root:
        return None
    if root.value == key:
        return root
    elif root.value < key:
        return bst_search(root.right, key)
    else:
        return bst_search(root.left, key)
