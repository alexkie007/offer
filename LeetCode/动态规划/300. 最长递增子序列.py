"""
给出一个无序的整形数组，找到最长上升子序列的长度。

例如，

给出 [10, 9, 2, 5, 3, 7, 101, 18]，
最长的上升子序列是 [2, 3, 7, 101]，因此它的长度是4。因为可能会有超过一种的最长上升子序列的组合，因此你只需要输出对应的长度即可。

你的算法的时间复杂度应该在 O(n2) 之内。

进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        dp = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] +1,dp[i])
        return max(dp)