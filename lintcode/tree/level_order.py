class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def level_order(root):
        if root is None:
            return []
        cur = [root]
        next = []
        result = []
        while cur:
            for node in cur:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
                result.append(node.val)
            cur = next
            next = []
        return result

    @staticmethod
    def level_order_2(root):
        if root is None:
            return []
        cur = [root]
        result = []
        while cur:
            node = cur.pop(0)
            if node.left:
                cur.append(node.left)
            if node.right:
                cur.append(node.right)
            result.append(node.val)
        return result

    @staticmethod
    def level_order_3(root):
        if root is None:
            return []
        cur = [root]
        result = []
        while cur:
            size = len(cur)
            level = []
            for i in range(size):
                node = cur.pop(0)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
                level.append(node.val)
            result.append(level)
        return result

    @staticmethod
    def zig_order(root):
        if root is None:
            return []
        cur = [root]
        next = []
        result = []
        is_odd = True
        while cur:
            for node in cur:
                if is_odd:
                    if node.right:
                        next.append(node.right)
                    if node.left:
                        next.append(node.left)
                else:
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)
                result.append(node.val)
            cur = next
            next = []
            is_odd = False if is_odd else True
        return result


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
print(s.level_order(a))
print(s.level_order_2(a))
print(s.level_order_3(a))
print(s.zig_order(a))
