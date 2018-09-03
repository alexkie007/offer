class Solution:
    def subsets(self, nums):
        if nums is None:
            return nums
        result = []
        list = []
        # nums.sort()
        self.subsets_helper(result, list, nums, 0)
        return result

    def subsets_helper(self, result, list, nums, index):
        result.append( "".join([x for x in list[:]]))
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            list.append(nums[i])
            self.subsets_helper(result, list, nums, i + 1)
            list.pop()
        return result


s = Solution()
print(s.subsets("122"))
