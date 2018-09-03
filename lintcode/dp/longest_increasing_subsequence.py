class Solution:
    def lis(self, nums):
        size = len(nums)
        f = [0 for i in range(size)]
        for i in range(size - 2, -1, -1):
            for j in range(size - 1, i, -1):
                if f[i] <= f[j] and nums[i] < nums[j]:
                    f[i] += 1
        max_value = max(f)
        result = []
        for i in range(size):
            if f[i] == max_value:
                result.append(nums[i])
                max_value -= 1
        return result


s = Solution()
print(s.lis( [10, 22, 9, 33, 21, 50, 41, 60, 80]))
