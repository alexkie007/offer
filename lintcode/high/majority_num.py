class Solution:
    def majority_num(self, nums):
        candidate = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            else:
                if candidate == nums[i]:
                    count += 1
                else:
                    count -= 1
        return candidate