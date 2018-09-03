'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''


class Solution:
    def IsBalanced_Solution1(self, pRoot):
        if pRoot == None:
            return pRoot
        if pRoot and pRoot.left is None and pRoot.right is None:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left - right) > 1:
            return False
        return self.IsBalanced_Solution1(pRoot.left) and self.IsBalanced_Solution1(pRoot.right)

    def TreeDepth(self, pRoot):
        if pRoot and pRoot.left is None and pRoot.right is None:
            return 1
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return 1 + max(left, right)


class Solution2:
    def __init__(self):
        self.flag = True

    def IsBalanced_Solution(self, pRoot):
        self.IsBalanced(pRoot)
        return self.flag

    def IsBalanced(self, pRoot):
        if not pRoot: return 0
        left = 1 + self.IsBalanced(pRoot.left)
        right = 1 + self.IsBalanced(pRoot.right)
        if abs(left - right) > 1:
            self.flag = False
        return max(left, right)
