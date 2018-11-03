'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
'''


def InversePairs(data):
    if len(data) <= 0:
        return 0
    count = 0
    copy = []

    for i in range(len(data)):
        copy.append(data[i])
    copy.sort()
    i = 0
    while len(copy) > i:
        count += data.index(copy[i])
        data.remove(copy[i])
        i += 1
    return count


class Solution:
    def reversePairs(self, nums):
        self.tmp = [0 for x in range(len(nums))]
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, start, end):
        if start >= end:
            return 0
        mid = (start + end) >> 1
        ans = self.merge_sort(nums, start, mid) + self.merge_sort(nums, mid + 1, end)
        i, j, k = start, mid + 1, start
        while i <= mid and j <= end:
            if nums[i] > nums[j]:
                self.tmp[k] = nums[j]
                j += 1
                ans += mid - i + 1
            else:
                self.tmp[k] = nums[i]
                i += 1
            k += 1
        while i <= mid:
            self.tmp[k] = nums[i]
            k += 1
            i += 1
        while j<= end:
            self.tmp[k] = nums[j]
            k+=1
            j+=1
        for i in range(start, end+1):
            nums[i] = self.tmp[i]
        return ans


print(InversePairs(
    [364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650, 418, 355, 460, 505, 360,
     965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233, 144, 174, 557, 67, 746, 550, 474, 162, 268, 142,
     463, 221, 882, 576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478, 147, 795, 380,
     973, 958, 115, 773, 870, 259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235, 187, 284, 665,
     874, 80, 45, 848, 38, 811, 267, 575]))
