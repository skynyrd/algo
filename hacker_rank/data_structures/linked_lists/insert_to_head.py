from common.LinkedList import LLNode


def insert(head: LLNode, data):
    if not head:
        head = LLNode(data)
        return head
    else:
        new_head = LLNode(data)
        new_head.next = head

    return new_head


node = LLNode(3)
node.next = LLNode(5)
node.next.next = LLNode(7)

insert(node, 8)
pass
