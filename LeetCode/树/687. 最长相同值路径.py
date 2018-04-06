"""
定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
"""

class Solution:
    def longestUnivaluePath(self, root):
        if root is None:
            return 0
        sub = max(self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))
        return max(sub, self.helper(root.left, root.val), self.helper(root.right, root.val))

    def helper(self, root, parent):
        if root is None or root.val != parent:
            return 0
        return 1 + max(self.helper(root.left, root.val), self.helper(root.right, root.val))