"""
给定一棵二叉树，返回其节点值的前序遍历。

例如：
给定二叉树[1,null,2,3]，

   1
    \
     2
    /
   3
返回 [1,2,3]。

注意: 递归方法很简单，你可以使用迭代方法来解决吗？
"""
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        stackNode = [root]
        while stackNode:
            node = stackNode.pop()
            res.append(node.val)
            if node.right:
                stackNode.append(node.right)
            if node.left:
                stackNode.append(node.left)
        return res
