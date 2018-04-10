class Solution:
    def lcse(self, str1, str2):
        dp = self.lcseCore(str1, str2)

        m = len(str1) - 1
        n = len(str2) - 1
        res = [""] * dp[m][n]
        index = len(res) -1
        while index >=0:
            if n >0 and dp[m][n] == dp[m][n-1]:
                n -= 1
            elif m>0 and dp[m][n] == dp[m-1][n]:
                m -= 1
            else:
                res[index] = str1[m]
                index -=1
                m -=1
                n -=1
        return res



    def lcseCore(self, str1, str2):
        m = len(str1)
        n = len(str2)
        dp = [([0] * n) for x in range(m) ]
        for i in range(1,m):
            dp[i][0] = max(dp[i-1][0],1 if str1[i] == str2[0] else 0)
        for i in range(1,n):
            dp[0][i] = max(dp[0][i-1],1 if str1[0] == str2[i] else 0)

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if str1[i] == str2[j]:
                    dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j])

        return dp

str1 = [2,4,3,1,2,1]
str2 = [1,2,3,2,4,1,2]
s= Solution()
print(s.lcse(str1,str2))



