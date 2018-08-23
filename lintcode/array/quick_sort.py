class Solution:
    def quick_sort(self, nums):
        if len(nums) > 0:
            mid = nums[0]
        else:
            return []
        l = [x for x in nums if x < mid]
        r = [x for x in nums if x > mid]
        return self.quick_sort(l) + [mid] + self.quick_sort(r)


s = Solution()
print(s.quick_sort([5, 4, 1, 2, 3, 4, 5, 6]))
