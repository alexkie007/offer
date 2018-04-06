"""

这是“每个节点的右向指针”问题的进阶。

如果给定的树可以是任何二叉树，该怎么办？你以前的解决方案仍然有效吗？

注意:

你只能使用恒定的空间。
例如，

给定以下二叉树，

         1
       /  \
      2    3
     / \    \
    4   5    7
调用你的函数后，树应该看起来像这样：

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""
"""
层次遍历
设立两个指针，一个指针的next指向每层的第一个，另外一个指针一直移动
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        while root:
            cur = temp = TreeLinkNode(0)
            while root:
                if root.left:
                    cur.next = root.left
                    cur = root.left
                if root.right:
                    cur.next = root.right
                    cur = root.right
                root = root.next
            root = temp.next