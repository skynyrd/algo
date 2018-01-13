# Algorithm explanation: https://www.youtube.com/watch?v=D2bIbWGgvzI&index=14&list=PLrmLmBdmIlpv_jNDXtJGYTPNQ2L1gdHxu

from common.Tree import TreeNode


def level_order_traverse_reverse(root: TreeNode):
    if not root:
        return None

    queue = [root]
    stack = []

    while len(queue) > 0:
        current = queue.pop(0)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        stack.append(current)

    while len(stack) > 0:
        print(stack.pop().value, end=" ")


# ex = TreeNode(4)
# bst_insert_iterative(ex, 3)
# bst_insert_iterative(ex, 10)
# bst_insert_iterative(ex, 7)
# bst_insert_iterative(ex, 5)
# bst_insert_iterative(ex, 2)
# print_tree(ex)
# print("*************")
# level_order_traverse_reverse(ex)
