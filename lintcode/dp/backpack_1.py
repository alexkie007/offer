"""
n个整数[1....n],装m的背包
"""


class Solution:
    def backpack_1(self, m, nums):
        f = [[False for x in range(len(nums) + 1)] for y in range(m + 1)]
        f[0][0] = True
        for i in range(len(nums)):
            for j in range(m + 1):
                f[i + 1][j] = f[i][j]
                if j >= nums[i] and f[i][j - nums[i]]:
                    f[i + 1][j] = True

        for i in range(m, -1, -1):
            if f[len(nums)][i]:
                return i
