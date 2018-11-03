class Solution:

    def permutations(self, nums):
        if nums is None or len(nums) < 2:
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

    def permutations1(self, nums):
        if nums is None or len(nums) < 2:
            return nums
        result = []
        list = []
        self.permutations_helper(result, list, nums)
        return result

    def permutations_helper(self, result, list, nums):
        if len(list) == len(nums):
            result.append(list[:])
            return
        for num in nums:
            if num not in list:
                list.append(num)
                self.permutations_helper(result, list, nums)
                list.pop()







s = Solution()
# print(s.permutations("abc"))
print(s.permutations1("abc"))
