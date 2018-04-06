"""
给出一个完全二叉树，求出该树的节点个数。

完全二叉树的定义如下：

在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含1~ 2h 个节点。
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftdepth = self.getLeftDepth(root)
        rightdepth = self.getRightDepth(root)
        if leftdepth == rightdepth:
            return pow(2, leftdepth) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def getLeftDepth(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count

    def getRightDepth(self, root):
        count = 0
        while root:
            count += 1
            root = root.right
        return count