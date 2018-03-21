'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''

import math

class Solution:
    def findMin(self, nums):
        if not nums:
            return False
        length = len(nums)
        left, right = 0, length-1

        while right - left >1:
            mid = (right+left)//2
            if nums[left] == nums[mid] == nums[right]:
                return min(nums)
            if nums[left] <= nums[mid]:
                left =mid
            if nums[right] >= nums[mid]:
                right = mid
        if right - left == 1:
            return nums[right]
        return nums[0]


Test = Solution()

print(Test.findMin([3, 4, 5, 6, 1, 2]))
print(Test.findMin([1, 0, 0, 1, 1, 1]))
print(Test.findMin([1, 1, 1, 0, 1]))
print(Test.findMin([1, 2, 3, 4, 5]))
print(Test.findMin([]))
print(Test.findMin([1]))
