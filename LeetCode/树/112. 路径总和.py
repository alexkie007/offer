"""
给定一棵二叉树和一个总和，确定该树中是否存在根到叶的路径，这条路径的所有值相加等于给定的总和。

例如：
给定下面的二叉树和 总和 = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在总和为 22 的根到叶的路径 5->4->11->2。
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


a = TreeNode(1)
b = TreeNode(2)
a.left = b
s = Solution()
print(s.hasPathSum(a, 1))