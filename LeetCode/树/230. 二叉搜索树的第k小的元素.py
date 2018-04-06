"""
给定一个二叉搜索树，编写一个函数kthSmallest来查找其中第k个最小的元素。

注意：
你可以假设k总是有效的，1≤ k ≤二叉搜索树元素个数。

进阶：
如果经常修改二叉搜索树（插入/删除操作）并且你需要频繁地找到第k小值呢？ 你将如何优化kthSmallest函数？
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """