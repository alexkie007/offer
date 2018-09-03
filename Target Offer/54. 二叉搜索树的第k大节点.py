'''
给定一颗二叉搜索树，请找出其中的第k大的结点。
例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode

    def KthNode(self, pRoot, k):
        self.res = []
        self.dfs(pRoot)
        return self.res[k - 1] if 0 < k <= len(self.res) else None

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.res.append(root)
        self.dfs(root.right)
