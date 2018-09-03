class Solution:
    def __init__(self):
        self.hash = []

    def dfs(self, x, y, n):
        if x == n:
            return 0
        if self.hash[x][y]:
            return self.hash[x][y]
        left = self.dfs(x + 1, y, n)
        right = self.dfs(x + 1, y + 1, n)
        self.hash[x][y] = min(left,right) +
