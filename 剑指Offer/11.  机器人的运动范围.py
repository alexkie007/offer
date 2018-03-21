import sys
sys.setrecursionlimit(1000000)

class Solution:
    def movingCount(self, threshold, rows, cols):
        count = 0
        visit = [0]*rows*cols
        #创建一个跟方格一样大小的矩阵，并且初始化元素全是False
        for i in range(rows*cols):
            visit[i] = False
        count = self.movingCountCore(threshold, rows, cols, 0, 0, visit)
        return count

    def movingCountCore(self, threshold, rows, cols, row, col, visit):
        count = 0

        if (self.check(threshold, rows, cols, row, col, visit)):
            visit[row * cols + col] = True

            count = (1 + self.movingCountCore(threshold, rows, cols, row-1, col, visit)
                    + self.movingCountCore(threshold, rows, cols, row, col-1, visit)
                    + self.movingCountCore(threshold, rows, cols, row+1, col, visit)
                    + self.movingCountCore(threshold, rows, cols, row, col+1, visit))
        return count



    def check(self, threshold, rows, cols, row, col, visit):
        if (row >= 0 and row < rows and col >= 0 and col < cols and self.getDigitSum(row) + self.getDigitSum(
                col) <= threshold and not visit[row * cols + col]):
            return True
        return False

    def getDigitSum(self, number):
        sum = 0
        while number > 0:
            sum += number % 10
            number /= 10
        return sum

s = Solution()
print(s.movingCount(5,10,10))