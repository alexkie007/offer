"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

此题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过1。



示例:

给定有序数组: [-10,-3,0,5,9],

一种可行答案是：[0,-3,9,-10,null,5]，它可以表示成下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return
        root = TreeNode(nums[length//2])
        root.left = self.sortedArrayToBST(nums[:length//2])
        root.right = self.sortedArrayToBST(nums[length//2+1:])
        return root