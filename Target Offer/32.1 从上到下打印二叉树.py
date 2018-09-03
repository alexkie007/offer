'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root == None:
            return []
        result = []
        curStack = [root]
        while curStack:
            nextStack = []
            for i in curStack:
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                result.append(i)
            curStack = nextStack
        return result
