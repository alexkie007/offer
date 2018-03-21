'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution:
    # array 二维列表
    def Find(self, target, array):

        # write code here
        rows = len(array)
        columns = len(array[0])
        row = 0
        column = columns -1
        while row < rows and column >=0:
            if array[row][column] == target:
                return True
            elif array[row][column] > target:
                column -=1
            else:
                row +=1
        return False
