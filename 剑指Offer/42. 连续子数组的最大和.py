

def maxsum(nums):
    sum = 0
    max_sum = 0
    for i in nums:
        if sum <=0:
            sum = i
        else:
            sum +=i
        max_sum = max(sum, max_sum)
    return max_sum


alist = [1, -2, 3, 10, -4, 7, 2, -5]

print(maxsum(alist))