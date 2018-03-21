def searchNum(nums):
    if nums == None or len(nums) <= 0:
        return False
    for i in nums:
        if i < 0 or i > len(nums) - 1:
            return False
    repeatNums = []
    copyNums = [ -1 for x in range(len(nums))]
    for i in range(len(nums)):
        if copyNums[nums[i]] == nums[i]:
            repeatNums.append(nums[i])
        else:
            copyNums[nums[i]] = nums[i]
    return repeatNums

a = [2, 3, 1, 0, 2, 5, 3]

print(searchNum(a))