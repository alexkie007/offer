
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.right= None
        self.left = None



class Solution:
    def lca(self, root, n1, n2):
        if root == None or n1 == None or n2 == None:
            return None
        if root == n1:
            return n1
        if root == n2:
            return n2
        left = self.lca(root.left, n1, n2)
        right = self.lca(root.right, n1, n2)
        if left != None and  right != None:
            return root
        elif left != None:
            return left
        elif right != None:
            return right
        else:
            return None



