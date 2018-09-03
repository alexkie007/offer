class Solution:
    @staticmethod
    def duplicate_nums(nums):
        if nums is None or len(nums) < 2:
            return
        for i in range(0, len(nums)):
            if nums[i] < 0 or nums[i] > (len(nums) - 1):
                return
        repeat_nums = set()
        for i in range(0, len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    repeat_nums.add(nums[i])
                    break
                else:
                    index = nums[i]
                    nums[index], nums[i] = nums[i], nums[index]
        return repeat_nums


s = Solution()
print(s.duplicate_nums([2, 3, 1, 0, 2, 5, 3]))
