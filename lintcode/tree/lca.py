class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def lca(self, root, a, b):
        if root is None or root == a or root == b:
            return root
        left = self.lca(root.left, a, b)
        right = self.lca(root.right, a, b)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None


