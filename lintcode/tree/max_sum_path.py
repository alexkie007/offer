class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sum = 0

    def max_sum(self, root):
        self.sum = root.val
        return max(self.one_path(root), self.sum)

    def one_path(self, root):
        if root is None:
            return 0
        left = self.one_path(root.left)
        right = self.one_path(root.right)
        self.sum = max(self.sum, max(0, left) + max(0, right) + root.val)
        return max(0, max(left, right)) + root.val


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

print(s.max_sum(a))
