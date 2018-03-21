'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def rearTree(self, sequence):
        length = len(sequence)
        root = sequence[-1]
        index = 0
        if min(sequence) > root or max(sequence) < root:
            return True
        for i in range(length-1):
            index = i
            if sequence[i]> root:
                break

        for j in range(index+1,length-1):
            if sequence[j] < root:
                return  False
        left = True
        if index >0:
            left = self.rearTree(sequence[:index])

        right = True
        if index > 0:
            right = self.rearTree(sequence[index:length-1])

        return left and right

array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.rearTree(array))

