from ctci.linked_lists.LLNode import LLNode
# not exact middle, any node but the first and last node


def delete_node(node: LLNode):
    if node is None or node.next is None:
        return False

    node.data = node.next.data
    node.next = node.next.next

    return True
