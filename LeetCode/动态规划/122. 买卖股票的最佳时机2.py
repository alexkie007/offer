"""
假设有一个数组，它的第 i 个元素是一个给定的股票在第 i 天的价格。

设计一个算法来找到最大的利润。你可以完成尽可能多的交易（多次买卖股票）。然而，你不能同时参与多个交易（你必须在再次购买前出售股票）。
"""
"""
解题思路：
如果第二天比第一天高，则卖出，卖出后又可以立刻买入
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        res = 0
        for i in range(len(prices)):
            if prices[i] < prices[i+1]:
                res += prices[i+1] - prices[i]
        return res