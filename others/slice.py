def slice(nums, start, stop, step):
    if step > 0:
        if start == None:
            start = 0
        if stop == None:
            stop = len(nums)
        if start  <= -len(nums):
            start = 0
        elif -len(nums) < start < 0 :
            start +=len(nums)
        if stop > len(nums):
            stop = len(nums)
        elif -len(nums) < stop < 0:
            stop += len(nums)

        if start > stop:
            return []
        res = []
        for i in range(start,stop, step):
            res.append(nums[i])
    if step < 0 :
        if start == None:
            start = -1
        if stop == None:
            stop = -1 - len(nums)
        if start > len(nums):
            start = -1
        elif 0 <= start < len(nums):
            start -=len(nums)
        if stop < -len(nums):
            stop = -1-len(nums)
        elif 0 <= stop <len(nums):
            stop -=len(nums)
        if start < stop:
            return  []
        res = []
        for i in range(start,stop, step):
            res.append(nums[i])
    return res

