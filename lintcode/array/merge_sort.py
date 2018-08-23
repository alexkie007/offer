class Solution:
    def merge_sort(self, nums):
        if len(nums) > 2:
            mid = len(nums) // 2
        elif len(nums) == 2:
            return [min(nums), max(nums)]
        else:
            return [nums[0]]
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0:
            return nums2
        if nums1[0] <= nums2[0]:
            num = nums1[0]
            nums1.remove(nums1[0])
        else:
            num = nums2[0]
            nums2.remove(nums2[0])
        return [num] + self.merge(nums1, nums2)


s = Solution()
print(s.merge_sort([1, 3, 4, 5, 2, 4, 5, 6, 7]))
