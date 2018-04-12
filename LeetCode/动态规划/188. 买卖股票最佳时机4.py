"""
假设你有一个数组，其中第 i 个元素是第 i 天给定股票的价格。

设计一个算法来找到最大的利润。您最多可以完成 k 笔交易。

注意:

你不可以同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
"""
解题思路：
解法的核心是假设手上最开始只有0元钱，那么如果买入股票的价格为price，手上的钱需要减去这个price，如果卖出股票的价格为price，手上的钱需要加上这个price。
它定义了4个状态：

Buy1[i]表示前i天做第一笔交易买入股票后剩下的最多的钱；

Sell1[i]表示前i天做第一笔交易卖出股票后剩下的最多的钱；

Buy2[i]表示前i天做第二笔交易买入股票后剩下的最多的钱；

Sell2[i]表示前i天做第二笔交易卖出股票后剩下的最多的钱；
"""
class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices):
            return sum(i-j for i,j in zip(prices[1:], prices[:-1]) if i-j >0)
        hold, release = [float("-inf")] *(k+1), [0] *(k+1)
        for p in prices:
            for i in range(1, k+1):
                release[i] = max(release[i], hold[i] + p)
                hold[i] = max(hold[i], release[i-1]-p)
        return release[k]

