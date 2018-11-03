
'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convert(self,root):
        if root == None:
            return root
        if not root.left and not root.right:
            return root


    def convert_node(self, tree, last):
        if not tree:
            return  None
        if tree.left:
            last = self.convert_node(tree.left, last)
        if last:
            last.right = tree
