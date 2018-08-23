"""
no more space
"""
class Solution:
    def merge_sorted_array(self, num1, m, num2, n):
        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1
        num1.extend([None] * n)
        while m != 0 and n != 0:
            if num1[m - 1] < num2[n - 1]:
                num1[m + n - 1] = num2[n - 1]
                n -= 1
            else:
                num1[m + n - 1] = num1[m - 1]
                m -= 1

        return num1


s = Solution()
print(s.merge_sorted_array([1, 2, 3], 3, [1, 2, 3, 4], 4))
