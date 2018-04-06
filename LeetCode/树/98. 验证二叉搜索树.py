"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

一个二叉搜索树有如下定义：

左子树只包含小于当前节点的数。
右子树只包含大于当前节点的数。
所有子树自身必须也是二叉搜索树。
示例 1：

    2
   / \
  1   3
二叉树[2,1,3], 返回 true.

示例 2：

    1
   / \
  2   3
二叉树 [1,2,3], 返回 false.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        res = []
        res = self.isValidBSTCore(root, res)
        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False
        return True

    def isValidBSTCore(self, root, result):
        if root is None:
            return
        self.isValidBSTCore(root.left, result)
        result.append(root.val)
        self.isValidBSTCore(root.right, result)
        return result

a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)
d = TreeNode(1)
e = TreeNode(2)
f = TreeNode(3)
a.left = b
a.right = c
d.left = e
d.right = f
s= Solution()
print(s.isValidBST(a))
print(s.isValidBST(d))