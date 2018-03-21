'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
    def NumberOf1(self, n):
        count = 0
        while n:
            count +=1
            n &= n-1
        return count

    def NumberOf2(self, n):
        if n >= 0:
            return bin(n).count('1')
        else:
            return bin(n + 2 ** 32).count('1')



s = Solution()
print(s.NumberOf2(2))