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

    def lca2(self, root, a, b):
        aex, bex, lca = self.helper(self, root, a, b)
        if aex and bex:
            return lca
        else:
            return None

    def helper(self, root, a, b):
        if root is None:
            return False, False, None

        laex, lbex, llca = self.helper(root.left, a, b)
        raex, rbex, rlca = self.helper(root.right, a, b)

        aex = laex or raex or root == a
        bex = lbex or rbex or root == b

        if root == a or root == b:
            return aex, bex, root
        if llca and rlca:
            return aex, bex, root
        if llca:
            return aex, bex, llca
        if rlca:
            return aex, bex, rlca
        return aex, bex, None
