"""
给定数组arr， 返回arr的最长递增子序列
如 arr=[2, 1, 5, 3, 6, 4, 8, 9, 7],
返回的最长递增子序列为[1,3,4,8,9]
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        时间复杂度O(n2)
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        dp = [1 for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] +1,dp[i])
        return max(dp)

    def lengthOfLIS2(self, nums):
        """
        时间复杂度O(nlogn)
        :type nums: List[int]
        :rtype: int
        """
        ends = [0] *len(nums)
        c = [nums[0]]
        for i in nums:
            if i <= c[0]:
                c[0] =i
            elif i > c[-1]:
                c +=i

        return
a = [2, 1, 5, 3, 6, 4, 8, 9, 7]
s = Solution()
print(s.lengthOfLIS(a))