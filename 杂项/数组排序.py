class Solution:
    def bubbleSort(self, nums):

        for i in range(len(nums)):
            flag = True
            for j in range(1,len(nums)-i):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                    flag = False
            if flag:
                return nums
        return nums

    # 每次选择未排序的最小的一个
    def selectSort(self, nums):
        length = len(nums)

        for i in range(length):
            min = i
            for j in range(i,length):
                if nums[j] < nums[min]:
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
        return nums

    def insertSort(self, nums):
        length = len(nums)
        for i in range(1,length):
            key = nums[i]
            j = i-1
            while j>=0:
                if nums[j] > key:
                    nums[j+1] = nums[j]
                    nums[j] = key
                j -=1
        return nums

    def quickSort(self, nums):
        length = len(nums)
        middle = nums[length//2]
        left = [x for x in nums if x < middle]
        right = [x for x in nums if x > middle]
        return self.quickSort(left) + [middle] + self.quickSort(right)

    def mergeSort(self, nums):
        length = len(nums)
        middle = length//2
        left = self.mergeSort(nums[:middle])
        right = self.mergeSort(nums[middle:])
        return self.merge(left, right)

    def merge(self,left, right):
        l, r = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l +=1
            else:
                result.append(right[r])
                r +=1
        result += left[l:]
        result += right[r:]
        return result


    def shellSort(self, nums):
        length = len(nums)
        gap = round(length/2)
        while gap >0:
            for i in range(gap, length):
                while i >= gap and nums[i-gap]>nums[i]:
                    nums[i], nums[i-gap] = nums[i -gap] ,nums[i]
                    i -= gap
            gap = round(gap/2)
        return nums


    def heapSort(self, nums):
        length = len(nums)
        self.buildHeap(nums, length)
        for i in range(length-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.adjustHeap(nums, 0,i)
    def buildHeap(self, nums, size):
        for i in range(size//2-1, -1, -1):
            self.adjustHeap(nums, i, size)

    def adjustHeap(self, nums, i, size):
        l = 2 * i +1
        r = 2 * i +2
        max = i
        if i < size/2:
            if l < size and nums[l] > nums[max]:
                max = l
            if r < size and nums[r] > nums[max]:
                max = r
            if max !=i:
                nums[max], nums[i] = nums[i], nums[max]
                self.adjustHeap(nums,max,size)
