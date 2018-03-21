
'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''





# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        B = []
        for i in A:
            mul_res = 1
            tmp = [j for j in A]
            tmp.remove(i)
            for x in tmp:
                mul_res *= x
                B.append(mul_res)
        return B
