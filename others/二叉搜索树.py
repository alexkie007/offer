class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        lastVisit = float("-inf")
    def insert(self, root, val):
        if root is None:
            root = TreeNode(val)
        else:
            if val < root.val:
                root.left = self.insert(root.left, val)
            elif val > root.val:
                root.right = self.insert(root.right, val)
        return root

    def query(self, root, val):
        if root is None:
            return
        if root.val == val:
            return root
        if root.val < val:
            return self.query(root.right, val)
        else:
            return self.query(root.left, val)

    def findMin(self, root):
        if root.left:
            return self.findMin(root.left)
        else:
            return root

    def delNum(self, root, val):
        if root is None:
            return
        if val < root.val:
            return self.delNum(root.left, val)
        elif val > root.val:
            return self.delNum(root.left, val)
        else:
            if root.left and root.right:
                tmp = self.findMin(root.right)
                root.val = tmp.val
                root.right = self.delNum(root.right, root.val)
            else:
                if root.left is None:
                    root = root.right
                elif root.right is None:
                    root = root.left
        return root

    def isBST(self, root):
        result = []
        result = self.isBSTCore(root, result)
        for i in range(1, len(result)):
            if result[i-1] >= result[i]:
                return False
        return True

    def isBSTCore(self, root, result):
        if root is None:
            return
        self.isBSTCore(root.left, result)
        result.append(root.val)
        self.isBSTCore(root.right, result)
        return result

    lastVisit = float("-inf")
    def isBST2(self, root):
        if root is None:
            return 1
        left = self.isBST2(root.left)
        if root.val >= self.lastVisit and left ==1:
            self.lastVisit = root.val
        else:
            return 0
        right = self.isBST2(root.right)
        return right

    def allBST(self, numbers):
        res = []
        if len(numbers) < 1:
            res.append("null")
            return res
        for i in numbers:
            left = self.allBST([x for x in numbers if x < i])
            right = self.allBST([x for x in numbers if x > i])
            for j in left:
                for k in right:
                    root = TreeNode(i)
                    root.left = j
                    root.right = k
                    res.append(root)
        return res


    def allBST2(self, n):
        return self.allBST2Core(1, n)

    def allBST2Core(self, start, end):
        res = []
        if start > end:
            res.append("null")
            return res
        for i in range(start, end+1):
            left = self.allBST2Core(start, i-1)
            right = self.allBST2Core(i+1, end)
            for j in left:
                for k in right:
                    root = TreeNode(i)
                    root.left = j
                    root.right = k
                    res.append(root)
        return res






s = Solution()
root=TreeNode(2)
root=s.insert(root, 1)
root=s.insert(root, 4)


print(s.query(root,2))
# root = s.delNum(root,2)
print(s.query(root,2))
print(s.isBST(root))