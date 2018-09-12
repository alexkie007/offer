"""
Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

f[i][j][t]前i个数取j个数出来能否和为t

1. 问是否可行 (DP) - f[x][0][0] = true
2. 问方案总数 (DP) - f[x][0][0] = 1
"""

class Solution:
    def k_sum(self, nums, k, target):
        f = [[[False for x in range(k+1)] for y in range(len(nums+1))] for z in range(target+1)]
        for i in range(len(nums)):
            for j in range(k):
                for t in range(target):
                    f[i+1][j+1][t] = f[i][j+1][t]
                    if t >= nums[i] and f[i][j][t-nums[i]]:
                        f[i+1][j+1][t] = f[i][j][t-nums[i]]

