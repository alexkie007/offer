class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.flag = True

    def is_balanced(self, root):
        self.is_balanced_core(root)
        return self.flag

    def is_balanced_core(self, root):
        if root is None:
            return 0
        left = self.is_balanced_core(root.left)
        right = self.is_balanced_core(root.right)
        if abs(left-right) >1:
            self.flag = False
        return 1 + max(left, right)


s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e

print(s.is_balanced(a))