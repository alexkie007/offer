class Solution:

    def permutations(self, nums):
        if nums is None or len(nums) <2:
            return nums
        result = []
        nums.sort()
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            temp = self.permutations(''.join(nums[:index]) + ''.join(nums[index + 1:]))
            for j in temp:
                result.append(nums[index] + j)
        return result


s = Solution()
print(s.permutations("abc"))
