class Solution:
    def merge_sorted_array(self, num1, num2):
        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1
        if num1[0] <= num2[0]:
            num = num1[0]
            num1.remove(num1[0])
        else:
            num = num2[0]
            num2.remove(num2[0])
        return [num] + self.merge_sorted_array(num1, num2)


s = Solution()
print(s.merge_sorted_array([1, 2, 3], [1, 2, 3,4]))
