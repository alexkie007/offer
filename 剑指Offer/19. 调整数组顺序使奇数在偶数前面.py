# class Solution:

def reorder( nums, func):
    left,right= 0, len(nums)-1
    while left< right:
        while  func(nums[left]):
            left += 1
        while not func(nums[right]):
            right -=1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    return nums

def iseven(num):
    return  num %2 ==1


print(reorder([1,2,3,4,5],func=iseven))

# s = Solution()
# a = s.reorder([1,2,3,4,5],func=iseven)
# print(a)