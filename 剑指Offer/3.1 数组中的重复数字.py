# def searchNum(nums):
#     nums_dict = {}
#     repeat_nums = []
#     for i in nums:
#         if i in nums_dict:
#             repeat_nums.append(i)
#         else:
#             nums_dict[i] = 0
#             nums_dict[i] += 1
#
#     return set(repeat_nums)


def searchNum1(nums):
    if nums == None or len(nums) <= 0:
        return False
    for i in nums:
        if i < 0 or i > len(nums) - 1:
            return False
    repeatNums = []
    for i in range(len(nums)):
        while nums[i] !=i:
            if nums[i] == nums[nums[i]]:
                repeatNums.append(nums[i])
                break
            else:
                index = nums[i]
                nums[i],nums[index] = nums[index],nums[i]


    return repeatNums


a = [2, 3, 1, 0, 2, 5, 3]

print(searchNum1(a))