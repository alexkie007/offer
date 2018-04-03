"""

"""

nums = [19, 7, 8, 25]
index = sorted(range(len(nums)), key = lambda i: nums[i])
count = 1
for i in range(1, len(index)):
    if index[i] > index[i-1]:
        count += 1
    else:
        break
print (len(index) - count)