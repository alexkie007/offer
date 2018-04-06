"""
给定一个二叉树，使用原地算法将它 “压扁” 成链表。



示例：

给出：

         1
        / \
       2   5
      / \   \
     3   4   6
压扁后变成如下：

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6


提示:

如果您细心观察该扁平树，则会发现每个节点的右侧子节点是以原二叉树前序遍历的次序指向下一个节点的。
"""
"""
The idea is very simple. Suppose n is the current visiting node, and p is the previous node of preorder traversal to n.right.

We just need to do the inorder replacement:
       *
       /
      n
   /     \
 left   right
  \ 
   *
    *
     \
      p
n.right - > n.left     
n.left -> NULL
p->right -> n.right
"""
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    prev = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.prev = root
        temp = root.right
        self.flatten(root.left)
        root.right, root.left = root.left, None
        self.prev.right = temp
        self.flatten(temp)