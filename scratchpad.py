class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order_traversal(tree: Node):
    if not tree:
        return None

    queue, stack = [tree], []

    while len(queue) > 0:
        curr = queue.pop(0)

        if curr.right:
            queue.append(curr.right)
        if curr.left:
            queue.append(curr.left)

        stack.append(curr)

    while len(stack) > 0:
        print(stack.pop().val)