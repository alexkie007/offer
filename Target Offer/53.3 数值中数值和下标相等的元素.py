'''
数组中数值和下表相等的元素
假设一个单调递增的数组里面每个元素都是整数且都是唯一的。
请编程实现一个函数，找出数组中任意一个数值等于其下标的元素。
例如，在数组【-3，-1，1，3，5]中，数字3和它的下标相等。
'''


class Solution:
    def FindIndexNumber(self, numbers):
        length = len(numbers)
        start = 0
        end = length - 1
        while start <= end:
            mid = int((end - start) / 2)
            if numbers[mid] == mid:
                return mid
            elif numbers[mid] > mid:
                end = mid - 1
            else:
                start = mid + 1
        return -1
