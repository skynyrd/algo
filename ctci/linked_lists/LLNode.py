class LLNode:
    def __init__(self, d):
        self.data = d
        self.next = None

    def append_to_tail(self, d):
        to_be_appended = LLNode(d)
        if self.next is None:
            self.next = to_be_appended
        else:
            node = self
            while node.next is not None:
                node = node.next
            node.next = to_be_appended

    def delete_element(self, d):
        node = self
        if node.data == d:
            node = node.next
        else:
            while node.next is not None:
                if node.next.data == d:
                    node.next = node.next.next
                else:
                    node = node.next