"""

给定一个序列（至少含有 1 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。

例如，给定序列 [-2,1,-3,4,-1,2,1,-5,4]，
连续子序列 [4,-1,2,1] 的和最大，为 6。



扩展练习:

若你已实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return float("-inf")
        curSum = 0
        maxSum = nums[0]
        for i in nums:
            curSum += i
            maxSum = max(curSum, maxSum)
            if curSum < 0:
                curSum = 0
        return maxSum

a = [-2,1, -3, 4, -1, 2 ,1, -5,4]
b = [-2,-1]
s = Solution()
print(s.maxSubArray(a))
print(s.maxSubArray(b))