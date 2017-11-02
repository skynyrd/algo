from ctci.linked_lists.LLNode import LLNode


def delete_dups(node: LLNode):
    dups = []
    prev = None

    while node is not None:
        if node.data in dups:
            prev.next = node.next
        else:
            dups.append(node.data)
            prev = node
        node = node.next


test_node = LLNode(4)
test_node.append_to_tail(3)
test_node.append_to_tail(3)
test_node.append_to_tail(3)
test_node.append_to_tail(4)
test_node.append_to_tail(5)
delete_dups(test_node)
pass


# If no buffer allowed:
def delete_dups_no_buffer(node: LLNode):
    current = node
    while current is not None:
        runner = current
        if runner.next is not None:
            if current.data == runner.next.data:
                runner.next = runner.next.next
            runner = runner.next
        current = current.next
