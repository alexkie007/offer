class Solution:
    def bad_count(self, nums):
        nums.sort()
        size = len(nums)
        bad_count = 0
        for i in range(size):
            for j in range(i, size):
                count = 0
                for k in range(3):
                    if nums[j][k] - nums[i][k] > 0:
                        count += 1
                    else:
                        break
                if count == 3:
                    bad_count += 1
                    break
        return bad_count


s = Solution()
size  = int(input())
nums = []
for i in range(size):
    nums.append([int(x) for x in input().split(" ") ] )
print(s.bad_count(nums))
