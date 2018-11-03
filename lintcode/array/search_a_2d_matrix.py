class Solution:
    @staticmethod
    def search_a_2_matrix(matrix, target):
        rows = len(matrix)
        if rows == 0:
            return False
        columns = len(matrix[0])
        if columns == 0:
            return False
        row = 0
        column = columns - 1
        while row <= rows - 1 and column >= 0:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                column -= 1
            else:
                row += 1
        return False


s = Solution()
matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]]
print(s.search_a_2_matrix(matrix, 3))
print(s.search_a_2_matrix(matrix, 20))
print(s.search_a_2_matrix(matrix, 35))
