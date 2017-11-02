class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def bst_insert(parent_node, node_to_insert):
    if parent_node is None:
        parent_node = node_to_insert
    else:
        if parent_node.value > node_to_insert.value:
            if parent_node.left is None:
                parent_node.left = node_to_insert
            else:
                bst_insert(parent_node.left, node_to_insert)
        else:
            if parent_node.right is None:
                parent_node.right = node_to_insert
            else:
                bst_insert(parent_node.right, node_to_insert)


node1 = Node(5)
bst_insert(node1, Node(6))
bst_insert(node1, Node(3))
bst_insert(node1, Node(1))
bst_insert(node1, Node(2))
bst_insert(node1, Node(4))

x = [1,3,2,5]
print(x[:3])
