class Solution:

    def subsets(self, nums):
        result = []
        list = []
        self.subsetsHelper(result, list, nums, 0)
        return result

    def subsetsHelper(self, result, list, nums, index):
        result.append(list[:])
        for i in range(index, len(nums)):
            list.append(nums[i])
            self.subsetsHelper(result, list, nums, i + 1)
            list.pop()
        return result


class Solution2:

    def subsets(self, nums):
        result = []
        list = []
        nums.sort()
        self.subsetsHelper(result, list, nums, 0)
        return result

    def subsetsHelper(self, result, list, nums, index):
        result.append(list[:])
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            list.append(nums[i])
            self.subsetsHelper(result, list, nums, i + 1)
            list.pop()
        return result


s = Solution()
print(s.subsets([1, 2, 3]))

s1 = Solution2()
print(s1.subsets([1, 2, 2]))
