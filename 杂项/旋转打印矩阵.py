
class Solution:
    def printMatrix(self, arr):
        rows = len(arr)
        cols = len(arr[0])
        start = 0
        ret = []
        while rows > 2* start and cols > 2 *start:
            self.printMatrixCore(arr,rows,cols,start,ret)
            start +=1
        return ret

    def printMatrixCore(self, arr, rows, cols, start, ret):
        endX = rows - 1 - start
        endY = cols - 1 - start
        # 从左到右
        for i in range(start, endY+1):
            ret.append(arr[start][i])
        # 从上到下
        if start<endX:
            for i in range(start+1, endX+1):
                ret.append(arr[i][endY])
        # 从右到左
        if start< endY and start < endX:
            for i in range(endY-1,start -1, -1):
                ret.append(arr[endX][i])
        # 从下到上
        if start < endX and start <endY-1:
            for i in range(endX-1,start,-1):
                ret.append(arr[i][start])
        return ret

    def printMatrix2(self, arr):
        rows = len(arr)
        cols = len(arr[0])
        start = 0
        ret1 = []
        ret2 = []
        while rows > 2* start and cols > 2 *start:
            self.printMatrix2Core(arr, rows, cols, start, ret1)
            self.printMatrix2Core(arr, rows, cols, start, ret2)
            start +=1
        return ret1, ret2

    def printMatrix2Core(self, arr, rows, cols, start, ret):
        endX = rows - 1 - start
        endY = cols - 1 - start
        # 从左到右
        for i in range(start, endY + 1):
            ret.append(arr[start][i])
        # 从上到下
        if start < endX:
            for i in range(start + 1, endX + 1):
                ret.append(arr[i][endY])
        # 从右到左
        if start < endY and start < endX:
            for i in range(endY - 1, start - 1, -1):
                ret.append(arr[endX][i])
        # 从下到上
        if start < endX and start < endY - 1:
            for i in range(endX - 1, start, -1):
                ret.append(arr[i][start])
        return ret

a = [
   [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
s= Solution()
print(s.printMatrix(a))

