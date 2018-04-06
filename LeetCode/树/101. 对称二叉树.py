"""
给定一个二叉树，检查它是否是它自己的镜像（即，围绕它的中心对称）。

例如，这个二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个 [1,2,2,null,3,null,3] 则不是:

    1
   / \
  2   2
   \   \
   3    3


说明:

如果你可以递归地和迭代地解决它就奖励你点数。
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isSymmetricCore(root, root)

    def isSymmetricCore(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None :
            return False
        if root1.val != root2.val:
            return False
        return  self.isSymmetricCore(root1.left, root2.right) and  self.isSymmetricCore(root1.right, root2.left)
