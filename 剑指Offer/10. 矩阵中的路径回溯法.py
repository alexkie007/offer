class Solution:

    def hasPath(self, matrix, rows, cols, path):
        if matrix == None or rows < 1 or cols < 1 or path == None:
            return False
        visited = [0] * (rows * cols)
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, martix, rows, cols, row, col, path, pathLength, visited):
        if len(path) == pathLength:
            return True
        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and martix[row* cols +col] == path[pathLength] and not visited[row * cols +col]:
            pathLength +=1
            visited[row *cols +col] = True

            hasPath = self.hasPathCore(martix, rows, cols, row, col-1, path, pathLength, visited) or \
                      self.hasPathCore(martix, rows, cols, row, col+1, path, pathLength, visited) or \
                      self.hasPathCore(martix, rows, cols, row-1, col, path, pathLength, visited) or \
                      self.hasPathCore(martix, rows, cols, row+1, col, path, pathLength, visited)
            if not hasPath:
                pathLength -=1
                visited[row*cols+col] = False

        return hasPath

s = Solution()
ifTrue = s.hasPath("ABCESFCSADEE", 3, 4, "ABCCED")
ifTrue2 = s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
print(ifTrue2)