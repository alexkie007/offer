"""
三步翻转法
"""


class Solution:

    def recover_rotated_array(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
        if nums[start] < nums[end]:
            return self.reverse(self.reverse(nums[:start]) + self.reverse(nums[start:]))
        else:
            return self.reverse(self.reverse(nums[:end]) + self.reverse(nums[end:]))

    def reverse(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return nums


s = Solution()
print(s.recover_rotated_array([4, 5, 1, 2, 3]))
print(s.reverse([1, 2, 3, 4, 5]))
