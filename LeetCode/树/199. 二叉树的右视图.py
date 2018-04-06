"""
给定一棵二叉树，想象自己站在它的右侧，返回从顶部到底部看到的节点值。

例如：
给定以下二叉树，

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
你应该返回 [1, 3, 4]。
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        curStack = [root]
        res = []
        while curStack:
            list = []
            nextStack = []
            while curStack:
                node = curStack.pop(0)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
                list.append(node.val)
            res.append(list[-1])
            curStack = nextStack
        return res

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
s = Solution()
print(s.rightSideView(a))