class TreeNode:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.right = None
        self.left = None


class Solution:
    def lca(self, root, n1, n2):
        if root is None or root == n1 or n2 == root:
            return root
        left = self.lca(root.left, n1, n2)
        right = self.lca(root.right, n1, n2)
        if left is not None and right is not None:
            return root
        return left if left is not None else right

    def lca2(self, root, n1, n2):
        if root is None or root == n1 or n2 == root:
            return root
        if n1.val < root.val and n2.val > root.val:
            return root
        elif n1.val < root.val and n2.val < root.val:
            return self.lca2(root.left, n1, n2)
        else:
            return self.lca2(root.right, n1, n2)

    def lca3(self, root, n1, n2):
        if root is None or root == n1 or n2 == root:
            return root
        path1 = []
        path2 = []
        self.findPath(root, n1, path1)
        self.findPath(root, n2, path2)
        return self.findLastCommonNode(path1, path2)

    def findPath(self, root, node, res):
        if root == node:
            res.extend(root)
            return True
        res.extend(root)
        found = False
        left = self.findPath(root.left, node, res)
        right = self.findPath(root.right, node, res)
        if not left and not right:
            res.pop()
        return found

    def findLastCommonNode(self, path1, path2):
        i = 0
        while i < len(path1.size) and i < len(path2.size):
            if path1[i] == path2[i]:
                res = path1[i]
            i += 1
        return res


s = Solution()

print()
