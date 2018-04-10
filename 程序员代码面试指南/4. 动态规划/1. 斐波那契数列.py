"""
给定整数N， 返回斐波那契数列的第N项
"""

class Solution:
    def Fibonacci(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b

s = Solution()
print(s.Fibonacci(2))