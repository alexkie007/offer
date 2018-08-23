class Solution:
    @staticmethod
    def find_min(nums):
        if nums is None:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= nums[end]:
                start = mid
            else:
                end = mid
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]


s = Solution()
print(s.find_min([3, 1, 2]))
print(s.find_min([1, 2, 3]))
print(s.find_min([4, 4, 2, 3]))
