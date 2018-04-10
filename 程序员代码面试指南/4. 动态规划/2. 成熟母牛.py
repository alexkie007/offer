"""
假设农场中的成熟的母牛每年只会生1头小母牛，并且永远不会死。第一年弄成有一只成熟的母牛，
从第2年开始，母牛开始生小母牛。每只小母牛3年之后成熟又可以生小母牛。给定整数N，求出N年后牛的数量
"""

class Solution:
    def Fibonacci(self, n):
        if n <1:
            return 0
        if n == 1 or n ==2 or n ==3:
            return n
        res =3
        pre =2
        prepre =1
        for i in range(4,n+1):
            tmp2 = res
            tmp1 = pre
            res = res+ prepre
            pre = tmp2
            prepre = tmp1
        return res

s = Solution()
print(s.Fibonacci(6))