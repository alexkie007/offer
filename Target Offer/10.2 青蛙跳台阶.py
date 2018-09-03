'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number < 2:
            return number
        a, b, c = 1, 0, 0
        for i in range(1, number + 1):
            c = a + b
            b = a
            a = c
        return c
