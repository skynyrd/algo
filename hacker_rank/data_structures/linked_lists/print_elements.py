from common.LinkedList import LLNode


def print_list(head: LLNode):
    while head is not None:
        print(head.data)
        head = head.next