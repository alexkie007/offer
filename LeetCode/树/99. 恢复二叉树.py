"""
二叉搜索树中的两个元素被错误地交换。

请在不改变其结构的情况下，恢复此树。

说明:
使用 O(n) 空间复杂度非常简单。你能否设计一个常量空间的解决方案？
"""
"""
解决思路：
先使用中序遍历二叉树，找到前一个节点大于后一个节点的两个数
分两种情况考虑，一种是任意两个节点交换，一种是相邻节点交换
Use a tree example: [100, 50, 200, 25, 75, 99, 400]
Sorted Order: 25,50,75,100,150,200,400
You can have out of order 50 and 200: 25,200,75,100,150,50,400. Notice in this case we have 2 out of order pairs: (200,75) and (150,50). Simply swap 200 and 50.
What if 25/50 or 200/400 are swapped? In that case we will have just one out of order element.
3 and 4 give us our algorithm.

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.order = []
        self.prev = None
        self.inOrder(root)
        if len(self.order) == 2:
            self.swap(self.order[0][0], self.order[1][1])
        elif len(self.order) ==1:
            self.swap(self.order[0][0], self.order[0][1])
        return

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        if self.prev and self.prev.val > root.val:
            self.order.append((self.prev, root))
        self.prev = root
        self.inOrder(root.right)
        return

    def swap(self, r1, r2):
        r1.val, r2.val = r2.val, r1.val
        return