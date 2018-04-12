'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
"""
解题思路：
先找到左右子树的分界点
然后递归左右子树
"""
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if length == 0:
            return False
        end = sequence[-1]
        mid = 0
        for j in range(length-1):
            mid = j
            if sequence[j] > end:
                break


        for j in range(mid+1,length-1):
            if sequence[j] < end:
                return False
        left = True
        right =True
        if mid >0:
            left = self.VerifySquenceOfBST(sequence[:mid])
        if mid < length -1:
            right = self.VerifySquenceOfBST(sequence[mid:length-1])
        return  left and  right
