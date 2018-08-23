class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def max_depth(self, root):
        if root is None:
            return 0
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
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
print(s.max_depth(a))