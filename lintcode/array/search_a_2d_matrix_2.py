class Solution:
    @staticmethod
    def search_a_2_matrix(matrix, target):
        rows = len(matrix)
        if rows == 0:
            return 0
        columns = len(matrix[0])
        row = 0
        column = columns - 1
        count = 0
        while row <= rows - 1 and column >= 0:
            if matrix[row][column] == target:
                count += 1
                column -= 1
            elif matrix[row][column] > target:
                column -= 1
            else:
                row += 1
        return count


s = Solution()
matrix = [[1, 3, 5, 7],
          [3, 4, 7, 8],
          [23, 30, 34, 50]]
print(s.search_a_2_matrix(matrix, 3))
print(s.search_a_2_matrix(matrix, 7))
print(s.search_a_2_matrix(matrix, 35))
