"""
给定数组arr， arr中所有的值都为正数且不重复。
每个值代表一种面值的货币，每种面值的货币可以使用任意张，
再给定一个正数aim岱庙要找的钱数，求换成aim的最少货币数
"""

class Solution:
    def minCoins1(self, arr, aim):
        """

        :param arr:
        :param aim:
        :return:
        """
        n = len(arr)
        maxValue = float("inf")
        dp = [([0]*(aim+1)) for i in range(n)]
        for i in range(1,aim+1):
            dp[0][i] = maxValue
            if i - arr[0] >=0 and dp[0][i-arr[0]] != maxValue:
                dp[0][i] = dp[0][i-arr[0]] + 1
        for i in range(1,n):
            for j in range(1,aim+1):
                left = maxValue
                if j - arr[i] >= 0 and dp[i][j-arr[i]] != maxValue:
                    left = dp[i][j-arr[i]] +1
                dp[i][j] = min(left, dp[i-1][j])
        return dp[n-1][aim] if dp[n-1][aim] != maxValue else -1

a = [2,3,5]
s = Solution()
print(s.minCoins1(a,20))
"""
给定数组arr, arr中所有的值都为正数。每个值仅代表一张钱的面值，再给定一个整数aim表示要找的钱数，求组成aim的最少钱数。

"""

class Solution2:
    def minCost(self, arr, aim):
        n = len(arr)
        dp = [([0] * (aim + 1)) for i in range(n)]
        maxValue = float("inf")
        for i in range(1, aim+1):
            dp[0][i] = maxValue
        if arr[0] <= aim:
            dp[0][arr[0]] = 1

        for i in range(1, n):
            for j in range(1, aim+1):
                left = maxValue
                if j-arr[i] >=0 and dp[i-1][j-arr[i]] != maxValue:
                    left = dp[i-1][j-arr[i]] + 1
                dp[i][j] = min(left, dp[i-1][j])
        return dp[n-1][aim] if dp[n-1][aim] != maxValue else - 1

a = [5,2,5,3]
b = [5,2,3]
s2 = Solution2()
# print(s.minCost(a,15))
print(s2.minCost(b,15))