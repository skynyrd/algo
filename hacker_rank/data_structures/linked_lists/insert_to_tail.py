from common.LinkedList import LLNode


def insert(head: LLNode, data):
    if not head:
        head = LLNode(data)
        return head
    else:
        ret = head
        while head.next is not None:
            head = head.next

        head.next = LLNode(data)

    return ret


node = LLNode(3)
node.next = LLNode(5)
node.next.next = LLNode(7)

insert(None, 8)
