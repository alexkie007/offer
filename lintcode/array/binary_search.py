class Solution:
    @staticmethod
    def binary_search(nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


s = Solution()
print(s.binary_search([1, 2, 3, 3, 4, 5], 3))
