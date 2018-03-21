'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def printTree(self, root):
        if root == None:
            return

        if root.left == None or root.right == None:
            return root
        nextLevel = 0
        toBePrinted = 1
        quene = []
        result = []
        quene .append(root)
        while len(quene) > 0:
            currentRoot = quene.pop(0)
            if currentRoot.left:
                quene.append(currentRoot.left)
                nextLevel +=1
            if currentRoot.right:
                quene.append(currentRoot.right)
                nextLevel +=1
            result.append(currentRoot.val)
            toBePrinted -=1
            if toBePrinted ==0:
                result.append('\n')
                toBePrinted = nextLevel
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
print(S.printTree(pNode1))