'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

class Solution:
    def rightClock(self, matrix):
        if matrix == None :
            return  False
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        ret = []
        while rows > 2 * start and columns > 2 * start:
            self.printCircle(matrix, rows, columns, start, ret)
            start +=1
        return  ret


    def printCircle(self, matrix ,rows, columns, start, ret):
        endX = columns - 1 - start  # 最后一列
        endY = rows - 1 - start  # 最后一行
        for i in range(start, endX+1):
            ret.append(matrix[start][i])
        if start < endY:
            for i in range(start+1, endY+1):
                ret.append(matrix[i][endX])
        if start < endX and start < endY:
            for i in range(endX-1, start -1,-1):
                ret.append(matrix[endY][i])
        if start < endX and start < endY -1:
            for i in range(endY -1 , start,-1):
                ret.append(matrix[i][start])
        return ret

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1],[2],[3],[4],[5]]
matrix3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
S = Solution()
S.rightClock(matrix)
S.rightClock(matrix2)
S.rightClock(matrix3)
print(S.rightClock(matrix2))
