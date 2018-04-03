"""
给定一个整数数列，找出其中和为特定值的那两个数。

你可以假设每个输入都只会有一种答案，同样的元素不能被重用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

"""
解题思路：
遍历数组，然后以数作为key， 索引位置作为value存到dict中
因此只需判断target- key是否已经存储在了dict中即可
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i, num in enumerate(nums):
            if target - num in map:
                return [map[target-num], i]
            map[num] =i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))