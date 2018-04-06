"""
给出一棵二叉树，寻找一条路径使其路径和最大。

对于这个问题，路径被定义为从树中任意节点连接任意节点的序列。该路径必须至少包含一个节点，并且不需要经过根节点。

例如：

给出一棵二叉树：

       1
      / \
     2   3
返回 6。
"""

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathSumCore(root)
        return self.res

    def maxPathSumCore(self, root):
        if root is None:
            return 0
        left = self.maxPathSumCore(root.left)
        right = self.maxPathSumCore(root.right)
        left = left if left>0 else 0
        right = right if right >0 else 0
        self.res = max(left+right+root.val, self.res)
        return max(left, right) + root.val