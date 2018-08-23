"""
time: O(log(m+n)
"""


class Solution:

    def median_of_two_sorted_array(self, num1, num2):
        size1 = len(num1)
        size2 = len(num2)
        if (size1 + size2) % 2 == 0:
            return (self.find_k_th(num1, size1, num2, size2, (size1 + size2) // 2 + 1) + self.find_k_th(num1, size1,
                                                                                                        num2, size2,
                                                                                                        (size1 + size2) // 2)) / 2
        else:
            return self.find_k_th(num1, size1, num2, size2, (size1 + size2) // 2)

    def find_k_th(self, num1, size1, num2, size2, k):
        if len(num1) > len(num2):
            return self.find_k_th(num2, size2, num1, size1, k)
        if len(num1) == 0:
            return num2[k - 1]
        if k == 1:
            return min(num1[0], num2[0])
        k1 = min(k // 2, size1)
        k2 = k - k1
        if num1[k1 - 1] > num2[k2 - 1]:
            return self.find_k_th(num1, size1, num2[k2:], size2 - k2, k - k2)
        elif num1[k1 - 1] < num2[k2 - 1]:
            return self.find_k_th(num1[k1:], size1 - k1, num2, size2, k - k1)
        else:
            return num1[k1 - 1]


s = Solution()

print(s.median_of_two_sorted_array([1, 2, 3, 4, 5], [2, 3, 4]))
print(s.median_of_two_sorted_array([1, 2, 3, 4, 5], [6, 7, 8]))
print(s.find_k_th([1, 2, 3, 4, 5], 5, [2, 3, 4], 3, 1))
