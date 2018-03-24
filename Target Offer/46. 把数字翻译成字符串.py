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

        return self.getTranslationCountCore(str(number))

    def getTranslationCountCore(self, number):
        length = len(number)
        counts = [0] * length

        # 从后往前递归查找
        for i in range(length-1, -1, -1):
            if i < length-1:
                count = counts[i+1]
            else:
                count = 1

            # 两位数可以合并
            if i < length -1:
                digit1 = int(number[i])
                digit2 = int(number[i+1])
                combine = digit1 * 10 + digit2

                if combine >= 10 and  combine <= 25:
                    if i < length -2:
                        count += counts[i+2]
                    else:
                        count += 1

            counts[i] = count

        return counts[0]

s= Solution()
print(s.getTranslationCount(12258))