"""
给定数组arr， arr中所有的值都为正数且不重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张，再给定一个正数代表要找的钱数，求换钱有多少种方法
"""

class Solution:
    def coins(self, coins ,aim):
        dp = [1 if i == 0 else 0  for i in range(aim+1)]
        for coin in coins:
            for i in range(coin, aim+1):
                dp[i] += dp[i-coin]

        return dp[-1]