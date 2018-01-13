class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def level_order_traverse(tree: Node):
    if tree:
        queue = []
        queue.append(tree)

        while len(queue) > 0:
