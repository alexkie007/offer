'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

class Solution:
    def Add(self, num1, num2):
        while num2:
            num1 ,num2 = (num1 ^ num2)& 0xFFFFFFFF ,(num1 & num2 ) <<1 & 0xFFFFFFFF
        return num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)