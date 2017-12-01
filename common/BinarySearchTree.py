from common.Tree import TreeNode


class BinarySearchTree(TreeNode):
    def __init__(self, value):
        super().__init__(value)

    def add(self, node_value):
        node = BinarySearchTree(node_value)
        if not self.value:
            self.value = node.value
        else:
            if node.value <= self.value:
                if self.left:
                    self.left.add(node.value)
                else:
                    self.left = node
            else:
                if self.right:
                    self.right.add(node.value)
                else:
                    self.right = node
