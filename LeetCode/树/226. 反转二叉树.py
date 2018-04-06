"""
翻转一棵二叉树。

     4
   /   \
  2     7
 / \   / \
1   3 6   9
转换为：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root