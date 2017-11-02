class Node:
    def __init__(self, adjacent, value):
        self.value = value
        self.adjacent = adjacent
        self.visited = False

    def make_visited(self):
        self.visited = True


node5 = Node([], 5)
node4 = Node([node5], 4)
node3 = Node([node4, node5], 3)
node2 = Node([node3], 2)
node1 = Node([node2], 1)


def search(root: Node):
    if root is None:
        return []

    print(root.value)
    root.make_visited()
    for node in root.adjacent:
        if not node.visited:
            search(node)


search(node2)
