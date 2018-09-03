from functools import reduce


class Solution:
    def combination_sum(self, nums, target):
        if nums is None:
            return nums
        result = []
        path = []
        self.helper(result, nums, 0, target, path)
        return result

    def helper(self, result, nums, start, target, path):
        length = len(nums)
        if target == 0:
            return result.append(path)
        for i in range(start, length):
            if target < nums[i]:
                return
            self.helper(result, nums, i, target - nums[i], path + [nums[i]])


s = Solution()
print(s.combination_sum([2, 3, 6, 7], 7))
