def is_div(a, b, c):
    for i in range(b):
        if a * i % b == c:
            return "YES"
    return "NO"


# num = int(input())
# nums =[]
# for i in range(num):
#     int_nums = [int(x) for x in input().split(" ")]
#     nums.append(int_nums)
# for num in nums:
#     print(is_div(num[0],num[1],num[2]))

#
# import math
#
#
# def lcm(nums):
#     ans = 1
#     for i in range(len(nums)):
#         ans = ans // math.gcd(ans, nums[i]) * nums[i]
#     return ans
#
#
# def min_m(n):
#     ans1 = lcm([n + 1, n + 1])
#     ans2 = lcm([x for x in range(1,n + 2)])
#     if ans1 == ans2:
#         return n + 2
#     i = n + 1
#     while ans1 != ans2:
#         i += 1
#         ans1 = lcm([ans1, i ])
#         ans2 = lcm([ans2, i])
#     return i
#
#
# n = int(input())
#
# # print(min_m(3))
# print(min_m(n))

# line_1 = [int(x) for x in input().split(" ")]
# n = line_1[0]
# m = line_1[1]
# map = {}
# for i in range(m):
#     line = [int(x) for x in input().split(" ")]
#     if line[0] in map.keys():
#         map[line[0]].append(line[1])
#     else:
#         map[line[0]] = [line[1]]
# new_map = map.copy()
#
#
# def in_map(i, map):
#     for key, value in map.items():
#         if i in value:
#             return True
#     return False
#
#
# def cal_x(i, map):
#     count = 0
#     if i in map.keys():
#         count += 1
#     has_visit = []
#     new_map = map[i]
#     while len(new_map) > 0:
#         a = map[i][0]
#         has_visit.append(a)
#         if a in map.keys():


    # return count


# def cal_x(i):

# print(map)
import random

print (random.randint(1, 10))