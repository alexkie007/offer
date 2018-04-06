"""
给定一个二叉树，返回其按层次遍历的节点值。 （即zhu'ceng'de，从左到右访问）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果为：

[
  [3],
  [9,20],
  [15,7]
]
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        curStack = [root]
        while curStack:
            nextStack = []
            list = []
            while curStack:
                node = curStack.pop(0)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
                list.append(node.val)
            res.append(list)
            curStack = nextStack
        return res
