"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        curStack = [root]
        res = []
        while curStack:
            nextStack = []
            list = []
            while curStack:
                node = curStack.pop(0)
                list.append(node.val)
                if node.left: nextStack.append(node.left)
                if node.right: nextStack.append(node.right)
            curStack = nextStack
            res.insert(0, list)
        return res

