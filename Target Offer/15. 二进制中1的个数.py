'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
"""
解题思路： 一个数与自己的减一相与，相当于把该数的最右边的1变成0， 二进制中有多少个1 就可以进行多少次这样的操作。
"""


class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n &= 0xffffffff
        while n:
            count += 1
            n &= n - 1
        return count

    def NumberOf2(self, n):
        if n >= 0:
            return bin(n).count('1')
        else:
            return bin(n + 2 ** 32).count('1')


s = Solution()
print(s.NumberOf2(2))
print(s.NumberOf1(-2))
