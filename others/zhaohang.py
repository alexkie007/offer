import math


class Solution:
    def min_k(self, a, b):
        a.sort()
        l = 1
        r = a[-1] + 1
        while l < r:
            m = (r - l) // 2 + 1
            h = 0
            for j in a:
                h += (j + m - 1) // m
            if h <= b:
                r = m
            else:
                l = m + 1
        return l


# a = input()
# a = [int(x) for x in a.split(" ")]
a = [3,6,7,11]
# b = int(input())
b=8
s = Solution()
print(s.min_k(a, b))
