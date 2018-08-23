class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.arr = []

    def pre_order(self, root):
        if root is None:
            return
        self.arr.append(root.val)
        if root.left:
            self.pre_order(root.left)
        if root.right:
            self.pre_order(root.right)

    def mid_order(self, root):
        if root is None:
            return
        if root.left:
            self.mid_order(root.left)
        self.arr.append(root.val)
        if root.right:
            self.mid_order(root.right)

    def mid_order_2(self, root):
        if root is None:
            return
        stack = []
        node = root
        result = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result



    def pos_order(self, root):
        if root is None:
            return
        if root.left:
            self.pos_order(root.left)
        if root.right:
            self.pos_order(root.right)
        self.arr.append(root.val)


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
c.left = f
s.pre_order(a)
print("pre_order", s.arr)
s.arr = []
s.mid_order(a)
print("mid_order", s.arr)

s.arr = []

print("mid_order", s.mid_order_2(a))
s.arr = []
s.pos_order(a)
print("pos_order", s.arr)
