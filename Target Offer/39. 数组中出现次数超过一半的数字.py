'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        dict = {}
        length = len(numbers)
        for i in numbers:
            if dict.get(i):
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1
            if dict[i] > length / 2:
                return i


a = [1, 2, 3, 2, 2, 2, 2, 2, 2, 5, 4, 2, 3, 3, 3]
s = Solution()
print(s.MoreThanHalfNum_Solution(a))
