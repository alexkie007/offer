'''
给你一根长度为n 的绳子，请把绳子剪成m段，
每段绳子的长度记为k[0],k[1],k[2],···,k[m].
请问k[0],k[1],k[2],···,k[m]可能的最大乘积是多少？
例如当绳子的长度是8时，我们把它剪成长度分别为2，3，3的三段，
此时得到的最大乘积是18
'''

class Solution:
    def maxProductAfterCutting(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length ==3:
            return 2
        products = [0] * (length+1)
        for i in range(4,length+1):
            max = 0
            for j in range(i//2):
                products[i] = products[i] * products[i-j]
                max = max(max,products[i])
            products.append(max)
        return  max

    def maxProductAfterCutting2(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        countOf3 = length//3
        if length - countOf3 *3 ==1:
            countOf3 -=1
        countOf2 = (length-countOf3*3)/2

        return countOf3 *3 +countOf2 *2





