'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''


class Solution:
    def Fibonacci(self, n):
        if n <= 0:
            return 0
        a, b, c = 1, 0, 0
        for i in range(n):
            c = a + b
            a, b = b, a + b
        return c


s = Solution()
# for i in range(30):
print(s.Fibonacci(3))
print(s.Fibonacci(4))
print(s.Fibonacci(5))
print(s.Fibonacci(6))
print(s.Fibonacci(7))
