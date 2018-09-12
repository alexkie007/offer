"""
edit_distance = max_length(a,b) - lcs(a,b)
"""

class Solution:
    def edit_distance(self, word1, word2):
        f = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            f[i][0] = i
        for j in range(len(word2) + 1):
            f[0][j] = j
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    f[i + 1][j + 1] = min(f[i][j], f[i][j + 1] + 1, f[i + 1][j] + 1)
                else:
                    f[i + 1][j + 1] = min(f[i][j + 1], f[i + 1][j], f[i][j]) + 1
        return f[len(word1)][len(word2)]


s = Solution()
print(s.edit_distance("mart", "karma"))
