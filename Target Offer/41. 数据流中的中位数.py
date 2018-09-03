'''
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''


class Solution:

    def __init__(self):
        self.nums = []

    def Insert(self, num):
        if len(self.nums) == 0:
            self.nums.append(num)
        else:
            i = len(self.nums) - 1
            while num > self.nums[i]:
                i -= 1
            self.nums.insert(i + 1, num)

        # write code here

    def GetMedian(self):
        length = len(self.nums)
        if length % 2 == 0:
            return ((self.nums[length // 2] + self.nums[length // 2 - 1])) / 2.0
        else:
            return self.nums[length // 2]
