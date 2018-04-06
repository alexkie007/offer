"""
给定一个整数 n，生成所有由 1...n 为节点组成的不同的二叉查找树。

例如，
给定 n = 3，则返回所有 5 种不同形态的二叉查找树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        return self.generateTreesCore(1, n)

    def generateTreesCore(self, start, end):
        res = []
        if start > end:
            return res
        for i in range(start, end+1):
            left = self.generateTreesCore(start, i-1)
            right = self.generateTreesCore(i+1, end)
            for j in left or [None]:
                    for k in right or [None]:
                        root = TreeNode(i)
                        root.left = j
                        root.right = k
                        res.append(root)
        return res

s = Solution()
res = s.generateTrees(3)


