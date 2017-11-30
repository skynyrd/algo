from typing import List

from common.Tree import TreeNode


def root_to_leaf_sum(root: TreeNode, sum, result: List[int]):
    if not root:
        return False

    if not root.left and not root.right:  # leaf node
        if root.value == sum:
            result.append(root.value)
            return True
        else:
            return False

    if root_to_leaf_sum(root.left, sum - root.value, result):
        result.append(root.value)
        return True

    if root_to_leaf_sum(root.right, sum - root.value, result):
        result.append(root.value)
        return True

    return False
