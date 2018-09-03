class Solution:
    def largest_rectangle_in_histogram(self, nums):
        l = self.find_first_min_in_left(nums)
        r = self.find_first_min_in_right(nums)
        max_value = 0
        for i in range(0, len(nums)):
            max_value = max(max_value, nums[i] * (l[i] - r[i]-1))
        return max_value
        # pass

    def find_first_min_in_left(self, nums):
        stack = []
        result = [x for x in range(0, len(nums))]
        stack.append(len(nums) - 1)
        for i in range(len(nums) - 2, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                # result[stack[-1]] = nums[i]
                stack.pop()
            if len(stack) > 0:
                result[i] = stack[-1]
            else:
                result[i] = i
            stack.append(i)
        return result

    def find_first_min_in_right(self, nums):
        stack = []
        result = [x for x in range(0,len(nums))]
        stack.append(0)
        for i in range(1, len(nums)):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                # result[stack[-1]] = nums[i]
                stack.pop()
            if len(stack) > 0:
                result[i] = stack[-1]
            else:
                result[i] = i
            stack.append(i)
        return result


s = Solution()
print(s.find_first_min_in_left([2, 1, 5, 6, 2, 3]))
print(s.find_first_min_in_right([2, 1, 5, 6, 2, 3]))

print(s.largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3]))
