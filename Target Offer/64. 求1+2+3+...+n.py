'''
求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

class Solution:
    def Sum_Solution(self, n):
        return sum(range(1,n+1))


    def Sum_Solution2(self, n):
        ans = n
        temp = n and self.Sum_Solution2(n-1)
        ans = ans +temp
        return ans
s= Solution()
print(s.Sum_Solution2(10))