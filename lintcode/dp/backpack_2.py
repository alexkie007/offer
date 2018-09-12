"""
n个物品，背包为m
体积a[1...n],价值v[1...n]
"""


class Solution:
    def backpack_2(self, n, m, weights, values):
        f = [[0 for x in range(m + 1)] for y in range(n + 1)]
        for i in range(m):
            f[0][i] = float("-inf")
        for i in range(n):
            for j in range(m):
                f[i+1][j+1] = max(f[i][j+1], f[i-1][j-weights[i]]+values[i])
        max_value = 0
        for i in range(m):
            max_value = max(max_value,f[n][i])
        return max_value