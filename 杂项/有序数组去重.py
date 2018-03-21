def removeduplicate(nums):
    newnums = []
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            i+=1
        else:
            newnums.append(nums[i])
    return newnums

a = [1,1,1,2,2,3,4,5,5,5,6]
print(removeduplicate(a))
