class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.flag = True

    def binary_search_tree(self, root):
        return self.is_valid(root)

    def is_valid(self, root):
        if root is None:
            return True
        if root.left:
            if root.left.val < root.val:
                return True
            else:
                return False
        if root.right:
            if root.right.val > root.val:
                return True
            else:
                return False
        left = self.is_valid(root.left)
        right = self.is_valid(root.right)
        return left and right


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
print(s.binary_search_tree(a))