'''
给定一个数字，我们按照如下规则把它翻译成字符串：
0翻译成a，1翻译成b,.....25翻译成z。
一个数字可能有多种翻译。
请编程实现一个函数，用来计算一个数组有多少种不同的翻译方法
'''

class Solution:
    def getTranslationCount(self, number):
        if number < 0:
            return 0

        return self.getTranslationCount(str(number))

    def getTranslationCountCore(self, number):
        length = len(number)
        counts = []
        count = 0
        for i in range(0,length,-1):
