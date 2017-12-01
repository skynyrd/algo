class Queue(object):
    def __init__(self):
        self.storage = []

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def dequeue(self):
        return self.storage.pop(0)

    def is_empty(self):
        return len(self.storage) < 1
