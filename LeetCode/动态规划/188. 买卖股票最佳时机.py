"""
假设你有一个数组，其中第 i 个元素是第 i 天给定股票的价格。

设计一个算法来找到最大的利润。您最多可以完成 k 笔交易。

注意:

你不可以同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""

class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
    