class Solution:
    def palindrom(self, nums):
        result = []
        path = []
        self.palindrom_helper(result, path, nums)
        return result

    def is_palindrom(self, nums):
        return nums[:] == nums[::-1]

    def palindrom_helper(self, result, path, nums):
        if not nums:
            result.append(path[:])
            return
        for i in range(1, len(nums) + 1):
            if self.is_palindrom(nums[:i]):
                self.palindrom_helper(result, path + [nums[:i]], nums[i:])


s = Solution()
print(s.palindrom("aab"))
