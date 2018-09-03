'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
例如，一支股票在某时间节点的价格为{9,11,8,5,7,12,16,14}.
如果我们能在价格为5的时候买入并在价格为16的时候卖出，则能收获最大的利润是11。
'''
"""
解题思路：
先令最小值为第一个值，
然后遍历数组，看前一个数是否小于最小值，若小于最小值，则替换
然后用当前值减去最小值，与当前最大差值进行比较
"""


class Solution:
    def MaxDiff(self, array):
        if array == [] and len(array) < 2:
            return 0
        min = array[0]
        maxDiff = array[1] = min
        for i in range(2, len(array)):
            if array[i - 1] < min:
                min = array[i - 1]
            curDiff = array[i] - min
            if curDiff > maxDiff:
                maxDiff = curDiff
        return maxDiff
