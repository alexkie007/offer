'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
"""
解题思路：
丑数是另一个丑数乘以2 3 5 的结果
因此我们可以每个丑数分别乘以2 3 5 
对于乘以2而言，一定存在某个丑数，排在它前面的每个丑数都小于当前已有丑数，在它之后每个丑数乘以2得到的结果都会太大
我们只需要记录这个值
对于3 5 类似
"""

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <=0:
            return 0
        n =1
        uglyNumber = [1] * index
        index2, index3, index5 = 0,0,0

        while n < index:
            minVal = min(uglyNumber[index2]*2, uglyNumber[index3]*3, uglyNumber[index5]*5)
            uglyNumber[n] = minVal
            while uglyNumber[index2]*2<= uglyNumber[n]:
                index2 +=1
            while uglyNumber[index3]*3<= uglyNumber[n]:
                index3 +=1
            while uglyNumber[index5]*5<= uglyNumber[n]:
                index5 +=1
            n +=1
        return uglyNumber[-1]

    def isUgly(self, num):
         while num % 2 == 0:
             num /= 2
         while num % 3 == 0:
            num /= 5
         while num % 3 == 0:
            num /= 5
         return True if num==1 else False

    def GetUglyNumber(self, index):
        
        number =0
        found = 0
        while found < index:
            number +=1
            found += 1  if self.isUgly(number) else 0
        return  number