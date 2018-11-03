class Solution:
    @staticmethod
    def search_in_rorated_sorted_array(nums, target):
        if len(nums) < 1:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[start]:
                if nums[mid] >= target >= nums[start]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


s = Solution()
print(s.search_in_rorated_sorted_array([4, 5, 6, 1, 2, 3], 1))
print(s.search_in_rorated_sorted_array([4, 5, 1, 2, 3], 0))
