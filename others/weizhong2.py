# import math
#
#
# def get_time(nums):
#     vol = 0
#     count = 0
#     for index, value in enumerate(nums):
#         if (index + 1) * (index + 1) * value / 36 > 1:
#             count += 1
#             value -=
#             vol += (index + 1) * (index + 1) * value
#     count = math.ceil(vol / 36.0)
#     return count
#
#
# _N = [int(x) for x in input().split(" ")]
# res = get_time(_N)
#
# print(res)
import math


# def get_min(nums):
#     room = [0, 5, 3, 1]
#     sum = 0
#     sum += (nums[5] + nums[4] + nums[3] + (nums[2] + 3) // 4)
#     n2 = 5 * nums[3] + room[nums[2] % 4]
#     if nums[1] > n2:
#         sum += (nums[1] - n2 + 8) / 9
#     n1 = 36 * (sum - nums[5]) - nums[1] * 2 * 2 - nums[2] * 3 * 3 - nums[3] * 4 * 4 - nums[4] * 5 * 5
#     if nums[0] > n1:
#         sum += (nums[0] - n1 + 35) // 36
#     return sum


def get_min(nums):
    countBox = 0
    if nums[0] == 0 and nums[1] == 0 and nums[2] == 0 and nums[3] == 0 and nums[4] == 0 and nums[5] == 0:
        return countBox
    countBox = nums[3] + nums[4] + nums[5] + (nums[2] + 3) // 4
    left2x2 = nums[3] * 5
    if nums[2] % 4 == 3:
        left2x2 += 1
    elif nums[2] % 4 == 2:
        left2x2 += 3
    elif nums[2] % 4 == 1:
        left2x2 += 5
    if left2x2 < nums[1]:
        countBox += (((nums[1] - left2x2) + 8) // 9)
    left1x1 = 36 * countBox - 36 * nums[5] - 25 * nums[4] - 16 * nums[3] - 9 * nums[2] - 4 * nums[1]
    if left1x1 < nums[0]:
        countBox += (((nums[0] - left1x1) + 35) // 36)
    return countBox


_N = [int(x) for x in input().split(" ")]
res = get_min(_N)

print(res)
