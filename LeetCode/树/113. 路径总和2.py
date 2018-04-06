"""
给定一个二叉树和一个和，找到所有从根到叶路径总和等于给定总和的路径。

例如，
给定下面的二叉树和 sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
"""

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        if root.val == sum and root.left is None and root.right is None:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+i for i in tmp]

    def pathSum2(self, root, sum):
        if root is None:
            return []
        res =[]
        self.pathSumCore(root, sum, [], res)
        return res

    def pathSumCore(self, root, sum, ls, res):
        if root.val == sum and root.left is None and root.right is None:
            ls.append(sum)
            res.append(ls)
        if root.left:
            self.pathSumCore(root.left, sum - root.val,ls+[sum],res)
        if root.right:
            self.pathSumCore(root.right, sum - root.val, ls + [sum], res)
