'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def MirrorTree(self, root):
        if root == None:
            return
        if root.left == None or root.right == None:
            return root
        pTemp = root.left
        root.left = root.right
        root.right = pTemp

        self.MirrorTree(root.left)
        self.MirrorTree(root.right)


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
S.MirrorTree(pNode1)
print(pNode1.right.left.val)