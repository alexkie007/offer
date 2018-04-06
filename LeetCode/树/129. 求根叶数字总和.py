"""
给定一个只包含 0-9 数字的二叉树，每个根到叶的路径可以代表一个数字。

例如，从根到叶路径 1->2->3则代表数字 123。

查找所有根到叶数字的总和。

例如，

    1
   / \
  2   3
根到叶子路径 1->2 表示数字 12。
根到叶子路径 1->3 表示数字 13。

返回总和 = 12 + 13 = 25。
"""
"""
解题思路：
每往下一层，就将当前的和乘以10倍，然后加上以一层的值
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumbersCore(root, 0)

    def sumNumbersCore(self, root, sum):
        if root is None:
            return 0
        sum = sum * 10 +root.val
        if root and not root.left and not root.right:
            return sum
        return self.sumNumbersCore(root.left, sum) + self.sumNumbersCore(root.right,sum)
