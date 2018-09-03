'''
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''


class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        if pRoot and pRoot.left == None and pRoot.right == None:
            return 1
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return 1 + max(left, right)
