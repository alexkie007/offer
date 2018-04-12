'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

class Solution:
    def reOrderArray(self, array):
        odd = [x for x in array if x % 2 ==1]
        right = [x for x in array if x % 2 ==0]
        odd.extend(right)
        return odd



    def iseven(self, num):
        return num % 2 == 1


    def reOrderArray3(self, array, func):
        start = 0
        end = len(array) -1
        while start < end:
            while func(array[start]):
                start += 1
            while not func(array[end]):
                end -= 1
            if start < end:
                array[start], array[end] = array[end], array[start]
        return array


a = [1,2,3,4,5,6]
s = Solution()
print(s.reOrderArray3(a, func=s.iseven))