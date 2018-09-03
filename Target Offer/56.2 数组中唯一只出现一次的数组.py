'''
数组中唯一只出现一次的元素

在一个数组中
'''


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        array.sort()
        result = []
        i = 0
        while i <= len(array) - 1:
            if i == len(array) - 1:
                result.append(array[i])
            if array[i] == array[i + 1] == array[i + 2]:
                i += 3
            else:
                result.append(array[i])
                i += 1
                break
        return result
