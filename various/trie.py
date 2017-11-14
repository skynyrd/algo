class Node(object):
    __slots__ = ['prefixes', 'children']

    def __init__(self):
        self.children = dict()
        self.prefixes = 0


class Trie(object):
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        word_index = 0
        while word_index < len(word):
            if not node.children.get(word[word_index]):
                node.children[word[word_index]] = Node()
                node = node.children[word[word_index]]
            else:
                node = node.children[word[word_index]]

            node.prefixes += 1
            word_index += 1

    def find(self, value):
        node = self.root
        value_index = 0
        while value_index < len(value):
            if not node.children.get(value[value_index]):
                return 0
            else:
                node = node.children[value[value_index]]
            value_index += 1
        return node.prefixes


a = int(input())
trie = Trie()

for i in range(a):
    b = input().split()
    if b[0] == 'add':
        trie.add(b[1])
    if b[0] == 'find':
        print(trie.find(b[1]))
