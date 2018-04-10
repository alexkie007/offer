"""
给定一个矩阵m， 从左上角开始每次只能向右或者向下走，最后达到右下角位置，
路径上所有的数字累加起来就是路径和，返回所有的路径中最小的路径和。
"""

"""
解题思路：
动过一个数组找到到每个位置到最小路径
"""
class Solution:

    def minPathSum(self, matrix):
        """
        时间复杂度O(MN) 空间复杂度O(MN)
        :param matrix:
        :return:
        """
        row = len(matrix)
        col = len(matrix[0])
        dp = [([0] * col) for i in range(row)] 
        dp[0][0] = matrix[0][0]
        for i in range(1,col):
            dp[0][i] = dp[0][i-1] + matrix[0][i]
        for j in range(1,row):
            dp[j][0] = matrix[j-1][0] + matrix[j][0]
        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
        return dp[row-1][col-1]

    def minPathSum2(self, matrix):
        """
        时间复杂度O(MN) 空间复杂度O(min{M,N})
        :param matrix:
        :return:
        """
        more = max(len(matrix),len(matrix[0]))
        less = min(len(matrix),len(matrix[0]))
        rowmore =  more == len(matrix)
        arr = [0] * less
        arr[0] = matrix[0][0]
        for i in range(1,less):
            arr[i] = arr[i-1] + (matrix[0][i] if rowmore else  matrix[i][0])
        for i in range(1, more):
            arr[0] = arr[0] + (matrix[i][0] if rowmore else matrix[0][i])
            for j in range(1,less):
                arr[j] = min(arr[j-1],arr[j] ) + (matrix[i][j] if rowmore else matrix[j][i] )
        return arr[less-1]




m = [
    [1,3,5,9],
    [8,1,3,4],
    [5,0,6,1],
    [8,8,4,0],
]
s = Solution()
print(s.minPathSum(m))
print(s.minPathSum2(m))