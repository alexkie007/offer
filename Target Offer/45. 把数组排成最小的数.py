'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

class Solution:
    def PrintMinNumber(self, numbers):
        if numbers == None:
            return None
        numbers.sort()
        while len(numbers)>1:
            numbers[0] = self.compare(numbers[0], numbers[1])
            numbers.remove(numbers[1])
        return numbers[0]

    def compare(self,x,y):
        s1 = str(x) +str(y)
        s2 = str(y) + str(x)

        if s1 > s2:
            return s2
        else:
            return s1


s = Solution()
a = [3, 32, 321]
print(s.PrintMinNumber(a))