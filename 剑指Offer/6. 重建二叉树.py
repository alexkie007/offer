class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def refactTree(self, pre, mid):
        if not pre and not mid:
            return None
        if set(pre) != set(mid):
            return None
        root = TreeNode(pre[0])
        i = mid.index(pre[0])
        root.left = self.refactTree(pre[1:i+1],mid[:i])
        root.right = self.refactTree(pre[i+1:],mid[i+1:])
        return root


pre = [1, 2, 3, 5, 6, 4]
mid = [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.refactTree(pre, mid)

def printNodeAtLevel(treeNode, level):
    if not treeNode or level <0:
        return 0
    if level == 0:
        print(treeNode.val)
        return 1
    printNodeAtLevel(treeNode.left, level-1)
    printNodeAtLevel(treeNode.right, level-1)


def PrintNodeByLevel(treeNode, depth):
    for level in range(depth):
        printNodeAtLevel(treeNode, level)

PrintNodeByLevel(newTree, 5)