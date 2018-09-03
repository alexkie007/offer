'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        result = []
        curStack = [root]
        odd = True
        while curStack:
            nextStack = []
            for i in curStack:
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
                result.append(i.val)
            result.append('\n')
            curStack = nextStack
        return result


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
print(S.PrintFromTopToBottom(pNode1))
