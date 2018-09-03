class Solution:
    def combination_sum_2(self, nums, target):
        result = []
        path = []
        nums.sort()
        self.helper(result, nums, path, 0, target)
        return result

    def helper(self, result, nums, path, index, target):
        if target == 0:
            return result.append(path[:])

        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.helper(result, nums, path, i + 1, target - nums[i])
            path.pop()


s = Solution()
print(s.combination_sum_2([10, 1, 6, 7, 2, 1, 5], 8))
