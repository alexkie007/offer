"""

给定两个二叉树，写一个函数来检查它们是否相同。

如果两棵树在结构上相同并且节点具有相同的值，则认为它们是相同的。



示例 1:

输入 :     1          1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入  :    1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
例 3:

输入 :     1          1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right
        return False


