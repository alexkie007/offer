"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶节点的最短路径的节点数量。
"""

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if root.left is None or root.right is None:
            return 1 + left + right
        return 1 + min(left, right)
