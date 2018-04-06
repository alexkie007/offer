"""
给定一个二叉树，确定它是高度平衡的。

对于这个问题，一棵高度平衡二叉树的定义是：

一棵二叉树中每个节点的两个子树的深度相差不会超过 1。

案例 1:

给出二叉树 [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

案例 2:

给出二叉树 [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""
"""
解题思路：
判断左右子树高度差是否小于1， 需要多次重复遍历，效率不高
可以设置一个标志位，然后递归求每个节点的深度，只要有一个节点的不平衡，就将标志位置位False

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = self.isBalancedCore(root.left)
        right = self.isBalancedCore(root.right)

        return abs(left-right) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalancedCore(self, root):
        if root is None:
            return 0
        left = self.isBalancedCore(root.left)
        right = self.isBalancedCore(root.right)
        return 1+max(left, right)

    flag = True
    def isBalanced2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isBalancedCore2(root)
        return self.flag

    def isBalancedCore2(self, root):
        if root is None:
            return 0
        left  = 1 + self.isBalancedCore2(root.left)
        right  = 1 + self.isBalancedCore2(root.right)
        if abs(left-right) >1:
            self.flag = False
        return max(left, right)

