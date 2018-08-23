class TreeNode:
    def __init__(self, value=None, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode


class Tree:
    def __init__(self, root=None):
        self.root = root

    def preOrder(self):
        if not self.root:
            return
        stackNode = []
        stackNode.append(self.root)
        while stackNode:
            node = stackNode.pop()
            print (node.value)
            if node.rightNode:
                stackNode.append(node.rightNode)
            if node.leftNode:
                stackNode.append(node.leftNode)

    def midOrder(self):
        if not self.root:
            return
        stackNode = []
        node = self.root
        while stackNode or node:
            while node:
                stackNode.append(node)
                node = node.leftNode
            node = stackNode.pop()
            print(node.value)
            node = node.rightNode

    def aftOrder(self):
        if not self.root:
            return
        stackNode = []
        markNode = None
        node = self.root
        while stackNode or node:
            while node:
                stackNode.append(node)
                node = node.leftNode
            node = stackNode.pop()
            if not node.rightNode or node.rightNode is markNode:
                # node  has no rightNode or node's rightNode has been checked
                print(node.value)
                markNode = node
                node = None
            else:
                stackNode.append(node)
                node = node.rightNode