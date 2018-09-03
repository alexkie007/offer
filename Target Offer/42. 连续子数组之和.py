'''
题目：输入一个整形数组，数组李有正数也有负数。数组中的一个或连续多个正数组成一个子数组。
求所有子数组的和的最地址。 要求时间复杂度为O(n).
'''


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == None:
            return array
        sum = 0
        maxSum = float("-inf")
        for i in range(len(array)):
            if sum < 0:
                sum = array[i]
            else:
                sum += array[i]
            maxSum = max(sum, maxSum)

        return maxSum


a = list(input().split())
a = [int(x) for x in a]
s = Solution()
print(s.FindGreatestSumOfSubArray(a))
