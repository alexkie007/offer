class Solution:
    def permutations(self, nums):
        if nums is None or len(nums) < 2:
            return nums
        result = []
        list = []
        self.permutations_helper(result, list, nums)
        return result

    def permutations_helper(self, result, list, nums):
        if len(list) == len(nums):
            count = self.InversePairs(list)
            if count ==3:
                result.append(list[:])
                return
        for num in nums:
            if num not in list:
                list.append(num)
                self.permutations_helper(result, list, nums)
                list.pop()

    def InversePairs(self, data):
        if len(data) <= 0:
            return 0
        count = 0
        copy = []
        for i in range(len(data)):
            copy.append(data[i])
        copy.sort()
        i = 0
        while len(copy) > i:
            count += data.index(copy[i])
            data.remove(copy[i])
            i += 1
        return count

n,t = [int(x) for x in input().split()]

s=Solution()
nums = [x for x in range(1,n+1)]
resutl =s.permutations(nums)
# result = []
# count_inverse = 0
# for i in resutl:
#     temp = i.copy()
#     count = InversePairs(i)
#     if count == t:
#         count_inverse +=1
#         result.append(temp)
# print(count_inverse)
# print(" ".join([ str(x) for x in result[0]]))