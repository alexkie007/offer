"""
给定一个二叉树，返回从根节点到叶节点的所有路径。

例如，给定以下二叉树:

   1
 /   \
2     3
 \
  5
所有根到叶路径是:

["1->2->5", "1->3"]
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        res = []
        self.binaryTreePathsCode(root, "", res)
        return res



    def binaryTreePathsCode(self, root, string, res):
        if not root.left and not root.right:
            res.append(string + str(root.val))
        if root.left:
            self.binaryTreePathsCode(root.left, string+str(root.val)+"->", res)
        if root.right:
            self.binaryTreePathsCode(root.right, string+str(root.val)+"->",res)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
a.left = b
a.right = c
c.right = d
s = Solution()
print(s.binaryTreePaths(a))