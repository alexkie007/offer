"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        curStack = [root]
        odd = 1
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

            res.append(list[::odd])
            curStack = nextStack
            odd *= -1
        return res

