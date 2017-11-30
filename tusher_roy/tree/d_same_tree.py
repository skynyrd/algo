from common.Tree import TreeNode


def same_tree(tree1: TreeNode, tree2: TreeNode):
    if tree1 is None and tree2 is None:
        return True

    if tree1 is None or tree2 is None:
        return False

    return tree1.value == tree2.value and same_tree(tree1.left, tree1.left) and same_tree(tree1.right, tree1.right)

# Complexity: O(n)
