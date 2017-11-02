from queue import Queue


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


def bfs(root: Node):
    nodes = []

    queue = Queue()
    root.make_visited()
    queue.put(root)

    while not queue.empty():
        node = queue.get()
        nodes.append(node.value)

        for n in node.adjacent:
            if not n.visited:
                n.make_visited()
                queue.put(n)

    return nodes

print(bfs(node1))

if 3 in [1,2] and 5 in [1,2]:
    print("s")