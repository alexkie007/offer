"""
假设你有一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来找到最大的利润。你最多可以完成两笔交易。

注意:

你不可同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
"""
那么用两个数组First，second分别array[:i]和array[i:]的最大利润。那么答案就等于max（First[i] + second[i + 1])。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size  = len(prices)
        if size ==0:
            return 0
        minValue = prices[0]
        ascMax = [0 ] * size
        desMax = [0 ] * (size +1)

        for i in range(len(prices)):
            minValue = min(minValue, prices[i])
            ascMax[i] = max(ascMax[i-1] , prices[i] - minValue)

        j = size -1
        maxValue = prices[size -1]
        while j >=0:
            maxValue = max(maxValue, prices[j])
            desMax[j] = max(desMax[j+1], maxValue- prices[j])
            j -=1

        maxProf = 0
        for i in range(len(prices)):
            maxProf = max(maxProf , ascMax[i] + desMax[i+1])
        return maxProf

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <=1:
            return 0
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0,0
        for p in prices:
            release2 = max(release2, hold2+p)
            hold2 = max(hold2, release1-p)
            release1 = max(release1, hold1+p)
            hold1 = max(hold1, -p)
        return release2


a = [2,1,2,0,1]
s= Solution()
print(s.maxProfit(a))