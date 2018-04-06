"""
给定一个二叉树

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
填充他的每个 next（下一个）指针，让这个指针指向其下一个右侧节点。如果找不到下一个右节点，则应该将 next（下一个）指针设置为 NULL。

初始状态下，所有 next（下一个）指针 都被设置为 NULL。

注意事项:

您只能使用恒定的额外空间。
你可以假设它是一棵完美二叉树（即所有叶子都在同一水平上，每个父节点有两个孩子）。


例如，鉴于以下完美二叉树，

         1
       /  \
      2    3
     / \  / \
    4  5  6  7
调用你的函数后，该树应该变成这样：

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""
"""
解题思路： 层序遍历的思想
如果左节点存在，则左节点的next节点是就是根节点的右子树，
如果右节点存在，则右节点的next节点 需要看根节点是否有next节点，若有，则为根节点next节点的左节点，若无则为None

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
        pre = root
        while root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
                root = root.next
            else:
                root = pre.left
                pre = root

    def connect2(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right:
            root.right.next = root.next.left if root.next else None
        self.connect(root.left)
        self.connect(root.right)
