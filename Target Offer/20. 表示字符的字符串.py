'''
将一个字符串转换成一个整数，
要求不能使用字符串转换整数的库函数。
 数值为0或者字符串不是一个合法的数值则返回0
 '''


class Solution:
    def StrToInt(self, s):
        try:
            return float(s)
        except:
            return 0


s = Solution()
print(s.StrToInt('121332313e3'))
