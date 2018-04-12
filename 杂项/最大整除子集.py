class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        if len(nums)<= 1:
            return nums
        nums.sort()
        dp = [1 for x in range(len(nums))]
        last = [-1 for x in range(len(nums))]
        max = 0
        idx = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    last[i] = j
            if max < dp[i]:
                max = dp[i]
                idx = i
        list = []
        while idx != -1:
            list.append(nums[idx])
            idx = last[idx]
        list.sort()
        return list

s = Solution()
print(s.largestDivisibleSubset([1,2,4,8]))
print(s.largestDivisibleSubset([1,2,3]))
print(s.largestDivisibleSubset([18,5]))
print(s.largestDivisibleSubset([3,4,16,8]))
print(s.largestDivisibleSubset([4,8,10,240]))