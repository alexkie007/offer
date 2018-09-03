'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。

'''
"""
解题思路：
先用一个队列存储 中序遍历的所有节点，
然后遍历队列，改变指针的方向
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return pRootOfTree
        self.arr = []
        self.midTraversal(pRootOfTree)
        for i, v in enumerate(self.arr[:-1]):
            v.right = self.arr[i + 1]
            self.arr[i + 1].left = v

        return self.arr[0]

    def midTraversal(self, Node):
        if Node is None:
            return Node
        self.midTraversal(Node.left)
        self.arr.append(Node)
        self.midTraversal(Node.right)
