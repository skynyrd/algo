from ctci.linked_lists.LLNode import LLNode


def print_kth_to_last(head: LLNode, k):
    if head is None:
        return 0

    index = print_kth_to_last(head.next, k) + 1
    if index == k:
        print(str(k) + "th to last node is " + str(head.data))

    return index


node = LLNode(3)
node.append_to_tail(4)
node.append_to_tail(5)
node.append_to_tail(6)
node.append_to_tail(8)
node.append_to_tail(9)

print_kth_to_last(node, 5)
