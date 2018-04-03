class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isCompleteBinaryTree(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        flag = 0
        queue = []
        queue.append(root)
        while queue:
            temp = queue.pop(0)
            if temp.left is not None:
                if flag == 1:
                    return False
                queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
                else:
                    flag = 1
            else:
                if temp.right is not None:
                    return False
                flag = 1
        return True
