class Solution:
    def maxProduct(self,numbers):
        minValue = numbers[0]
        maxproduct = 0
        for i in range(1,len(numbers)):
            minValue = min(minValue, numbers[i])
            maxproduct = max(maxproduct, numbers[i] - minValue)

        return maxproduct

a = [9,11,8,5,7,12,16,14]
s = Solution()
print(s.maxProduct(a))
