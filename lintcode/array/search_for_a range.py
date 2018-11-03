class Solution:
    @staticmethod
    def search_for_a_range(nums, target):
        if len(nums) == 0:
            return [-1,-1]
        start = 0
        end = len(nums) - 1
        bound = [-1, -1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            bound[0] = start
        elif nums[end] == target:
            bound[0] = end
        else:
            bound[0] = bound[1] = -1
            return bound

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            bound[1] = end
        elif nums[start] == target:
            bound[1] = start
        else:
            bound[0] = bound[1] = -1
            return bound
        return bound


s = Solution()
print(s.search_for_a_range([1, 2, 2, 3, 4, 5], 2))
print(s.search_for_a_range([1, 3,5,6,8,9], 7))
