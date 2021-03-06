"""
给定一棵树的前序遍历与中序遍历，依据此构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 = [3,9,20,15,7]
中序遍历 = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return
        start = preorder[0]
        index = inorder.index(start)
        root = TreeNode(start)
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
