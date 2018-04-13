'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
"""
解题思路：
每个数异或自己都为0，所以可以考虑从头到尾异或，最后不为0的数就是只出现一次的数

因为有两个数只出现一次，因此可以考虑将数组分成两部分，每个部分只有一个出现一次的数

首先我们从头到尾异或遍历一遍数组，最终得到的结果就是两个只出现一次的数字异或的结果
由于两个数字不一样，所以异或的结果至少有一位为1，我们在数字中找到第一个为1的位置，记为n，
然后以第n位是不是1 将数组分为两部分

最后遍历遍历一次，就可以找到两个只出现1次的数
"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        array.sort()
        result = []
        i = 0
        while i <= len(array) - 1:
            if i == len(array)-1:
                result.append(array[i])
                break
            if array[i] == array[i + 1]:
                i += 2
            else:
                result.append(array[i])
                i += 1

        return result

    def FindNumsAppearOnce2(self, array):
        tmp = 0
        for i in array:
            tmp ^= i
        idx = 0
        while (tmp &1)==0:
            tmp >>=1
            idx +=1
        a = b =0
        for i in array:
            if self.isBit(i, idx):
                a ^=i
            else:
                b ^=i
        return [a, b]

    def isBit(self,number, index):
        number >>= index
        return number & 1
s = Solution()
print(s.FindNumsAppearOnce([2,4,3,6,3,2,5,5]))