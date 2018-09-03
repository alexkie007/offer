class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[len(A), len(A)] for i in range(len(A))]
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] + 1

            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                dp[i][0] = min(dp[i][0], dp[i - 1][1])
                dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)

        return min(dp[len(A) - 1][0], dp[len(A) - 1][1])


# a = "ccdcc"
# b = "ccccd"
a = [3, 3, 4, 3, 3]
b = [3, 3, 3, 3, 4]
s = Solution()
print(s.minSwap(a, b))
