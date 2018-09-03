'''
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        return self.isSymmerticalHelper(pRoot, pRoot)

    def isSymmerticalHelper(self, pRoot1, pRoot2):
        if pRoot1 is None and pRoot2 is None:
            return True
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmerticalHelper(pRoot1.left, pRoot2.right) and self.isSymmerticalHelper(pRoot1.lright,
                                                                                                pRoot2.left)
