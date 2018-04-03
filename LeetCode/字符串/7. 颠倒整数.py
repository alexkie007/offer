"""
给定一个范围为 32 位 int 的整数，将其颠倒。

例 1:

输入: 123
输出:  321


例 2:

输入: -123
输出: -321


例 3:

输入: 120
输出: 21
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max =  2147483648
        min = -2147483648
        if x > max or x <min:
            return 0
        if x >= 0:
            res = int(str(x)[::-1])
            return  res if res <max else 0
        else:
            res = -1 * int(str(abs(x))[::-1])
            return res if res> min else 0



s = Solution()
print(s.reverse(1534236469))