'''
0~ n-1中缺失的数字
一个长度为n-1的递增排序数组中所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字有且只有一个数字不在该数组中，请找出这个数字
'''

class Solution:
    def FindLostNumber(self, numbers):
        length = len(numbers)
        start = 0
        end = length  -1
        while start <= end:
            mid = int((end- start)/2)
            if mid == numbers[mid]:
                start = mid +1
            else:
                if mid ==0 or numbers[mid-1] == mid -1:
                    return mid
                end = mid - 1
        if start == length:
            return length
        return -1