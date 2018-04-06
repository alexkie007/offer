class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归解法
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        list = []
        left = self.inorderTraversal(root.left)
        list.append(root.val)
        right = self.inorderTraversal(root.right)
        return left + list + right

    # 循环解法
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stackNode = []
        node = root
        res = []
        while stackNode or node:
            while node:
                stackNode.append(node)
                node = node.left
            node = stackNode.pop()
            res.append(node.val)
            node = node.right
        return res

        return left + list + right