def insertSort(nums):
    count = len(nums)
    for i in range(1,count):
        key = nums[i]
        j = i-1
        while j >= 0:
            if nums[j] >key:
                nums[j+1] = nums[j]
                nums[j] = key
    return nums
