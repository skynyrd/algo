from common.Queue import Queue


class HuffmanTree:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


def decodeHuff(root: HuffmanTree, s):
    current = root
    result = ""

    for char in s:
        if char == "1":
            current = current.right
        else:
            current = current.left
        if not current.left and not current.right:
            result += current.data
            current = root

    print(result)

test_tree = HuffmanTree(5, '\0')
test_tree.right = HuffmanTree(3, 'A')
test_tree.left = HuffmanTree(2, '\0')
test_tree.left.left = HuffmanTree(1, 'B')
test_tree.left.right = HuffmanTree(1, 'C')

decodeHuff(test_tree, "1001011")
