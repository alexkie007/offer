'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''

def searchNum1(nums):
    if nums == None or len(nums) <= 0:
        return False
    for i in nums:
        if i < 0 or i > len(nums) - 1:
            return False
    repeatNums = []
    for i in range(len(nums)):
        while nums[i] !=i:
            if nums[i] == nums[nums[i]]:
                repeatNums.append(nums[i])
                break
            else:
                index = nums[i]
                nums[i],nums[index] = nums[index],nums[i]


    return repeatNums

from collections import Counter

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers):
        count = Counter(numbers).most_common()[0][0]
        if count >1:
            return "true, %s"%( count)
        else:
            return False

    def duplicateNums(self, numbers):
        if numbers == None or len(numbers) < 1:
            return False
        for i in numbers:
            if i < 0 or i >len(numbers) -1:
                return False
        duplicate = []
        for i in range(len(numbers)):
            while i != numbers[i]:
                if numbers[i] == numbers[numbers[i]]:
                    duplicate.append(numbers[i])
                    break
                temp = numbers[i]
                numbers[i] = numbers[temp]
                numbers[temp] = temp
        return duplicate

s = Solution()
print(s.duplicateNums([2,3,1,0,2,5,3]))
print(s.duplicateNums([2,3,2,3,0,1]))

