"""
给出 n，问由 1...n 为节点组成的不同的二叉查找树有多少种？

例如，
给出 n = 3，则有 5 种不同形态的二叉查找树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
"""
解题思路：
卡特兰数
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] *(n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[n]

s = Solution()
print(s.numTrees(3))