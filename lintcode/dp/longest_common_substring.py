class Solution:
    def lcs(self, nums1, nums2):
        f = [[0 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
        for i in range(0, len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = 0
        max_value = 0
        for x in range(len(f)):
            for y in range(len(f[0])):
                max_value = max(max_value, f[x][y])
        return max_value


s = Solution()
print(s.lcs("ABCD", "EABC"))
