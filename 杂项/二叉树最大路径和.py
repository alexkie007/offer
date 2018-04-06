"""
给出一棵二叉树，寻找一条路径使其路径和最大，路径可以在任一节点中开始和结束（路径和为两个节点之间所在路径上的节点权值之和）

样例
给出一棵二叉树：

       1
      / \
     2   3
返回 6


"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    sum = float("-inf")
    def maxPathSum(self, root):
        self.sum = root.val
        def onePath(root):
            if root is None:
                return 0
            l = onePath(root.left)
            r = onePath(root.right)
            self.sum = max(self.sum , max(0, l) + max(0, r) + root.val)
            return max(0, max(l, r)) + root.val
        return max(onePath(root), self.sum)



a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
s = Solution()
print(s.maxPathSum(a))