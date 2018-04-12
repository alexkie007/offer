'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵：
    [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
    则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        result =[]
        while rows > 2 * start and columns > 2 * start:
            start +=1
        return result

    def printCycle(self, matrix, rows, columns, start, ret):
        endX = rows - 1 - start
        endY = columns - 1 - start
        # 从左往右
        for i in range(start, endY + 1):
            ret.append(matrix[start][i])
            # 从上往下 至少存在两行
        if start < endX:
            for i in range(start + 1, endX + 1):
                ret.append(matrix[i][endY])
        # 从右往左 至少存在两列
        if start < endX and start < endY:
            for i in range(endY - 1, start - 1, -1):
                ret.append(matrix[endX][i])
        # 从下往上 至少三行两列
        if start < endY and start < endX - 1:
            for i in range(endX - 1, start, -1):
                ret.append(matrix[i][start])
        return ret
