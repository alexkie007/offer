'''(
打印从1到最大的n位数
输入数字n，按顺序打印出1到最大的n位十进制数。
比如输入3，则打印出1、2、3一直到3位数的999
'''


class Solution:
    def prin1ToMax(self, number, length, index):
        if index == length - 1:
            print(int(''.join(number)))
            return
        for i in range(10):
            number[index + 1] = str(i)
            self.prin1ToMax(number, length, index + 1)

    def print1ToMaxOfDigits(self, n):
        if n <= 0: return
        number = ['0'] * n
        for i in range(10):
            number[0] = str(i)
            self.prin1ToMax(number, n, 0)


s = Solution()
print(s.print1ToMaxOfDigits(3))
