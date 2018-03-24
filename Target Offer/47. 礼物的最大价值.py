'''
在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或者向下移动一格，知道到达棋盘的右下角。
给定一个棋盘及其上面的礼物，请计算你最多能拿多少价值的礼物？
'''
class Solution:
    def getMaxValue(self, values, rows, cols):
        if len(values) ==0 or rows<=0 or cols <=0:
            return 0
        maxValues = [0] * cols
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = maxValues[j]
                if j > 0:
                    left = maxValues[j-1]
                maxValues[j] = max(up,left) + values[i*cols+j]

        maxValue = maxValues[cols-1]
        return maxValue