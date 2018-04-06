
'''
输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSubTree(self, root1, root2):
        if root1 and root2 :
            if root1.val == root2.val:
                return self.isSubTree(root1.left, root2.left ) and self.isSubTree(root1.right, root2.right)
            else:
                return self.isSubTree(root1.left, root2) or self.isSubTree(root1.right, root2)
        if not root1 and root2:
            return False
        return True

    def isMatch(self, s, t):
        if not (s and t):
            return s is t
        return (s.val == t.val and
                self.isMatch(s.left, t.left) and
                self.isMatch(s.right, t.right))

    def isSubTree2(self, s, t):
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubTree2(s.left, t) or self.isSubTree2(s.right, t)

pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.isSubTree2(pRoot1, pRoot8))