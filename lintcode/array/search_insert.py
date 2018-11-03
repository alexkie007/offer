class Solution:
    @staticmethod
    def search_insert(nums, target):
        if len(nums) == 0 :
            return 0
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[start] >= target:
            return start
        elif nums[end] >= target:
            return end
        else:
            return end + 1


s = Solution()
print(s.search_insert([1, 3, 5, 6], 5))
print(s.search_insert([1, 3, 5, 6], 2))
print(s.search_insert([1, 3, 5, 6], 7))
print(s.search_insert([1, 3, 5, 6], 0))
