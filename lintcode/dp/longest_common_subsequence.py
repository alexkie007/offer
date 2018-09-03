class Solution:
    def lcs(self, nums1, nums2):
        f = [[0 for i in range(len(nums2) + 1)] for j in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
        return f[len(nums1)][len(nums2)]


s = Solution()
print(s.lcs("ABCD", "EACB"))
