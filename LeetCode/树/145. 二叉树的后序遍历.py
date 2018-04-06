"""
给定一棵二叉树，返回其节点值的后序遍历。

例如：
给定二叉树 [1,null,2,3]，

   1
    \
     2
    /
   3
返回 [3,2,1]。

注意: 递归方法很简单，你可以使用迭代方法来解决吗？
"""

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stackNode = []
        node = root
        markNode = None
        res = []
        while stackNode or node:
            while node:
                stackNode.append(node)
                node = node.left
            node = stackNode.pop()
            if node.right is None or node.right is markNode:
                res.append(node.val)
                markNode = node
                node = None
            else:
                stackNode.append(node)
                node = node.right
        return res
