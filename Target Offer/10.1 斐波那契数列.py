'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

class Solution:
    def Fibonacci(self, n):
        if n <= 0 or n > 39:
            return 0
        a, b, c = 1, 0, 0
        for i in range(n):
            c = a +b
            b = a
            a = c
        return c