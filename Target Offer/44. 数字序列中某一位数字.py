'''
数字以0123456789101112131415···的格式序列化到一个字符序列中。
在这个序列中，第5位是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。
'''

class Solution:
    def digitAtIndex(self,index):
        if index <0:
            return -1
        digits =1
        while True:
            numbers = self.countOfIntegers(digits)
            if index < numbers *digits:
                return self.digitAtIndexCore(index,digits)

            index -= digits*numbers
            digits +=1


     # n位数有几个
    def countOfIntegers(self, digits):
        if digits==1:
            return 10
        count = pow(10, digits-1)
        return 9 * count

    # n位数的第一个数字
    def beginNumber(self, digits):
        if digits == 1:
            return 10
        return pow(10, digits-1)

    #
    def digitAtIndexCore(self, index, digits):
        # index 所出数字是n位数的第number个
        number = self.beginNumber(digits) + index//digits
        indexFromRight = digits - index %digits

        for i in range(1, indexFromRight):
            number /= 10
        return number %10

s = Solution()
print(s.digitAtIndex(1001))