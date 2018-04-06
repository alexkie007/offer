class Solution:
    def maxDistance(self, root):
        if root.left is None and root.right is None:
            return 0
        max_distance = 1
        self.maxDistanceCore(root, max_distance)
        return max_distance

    def maxDistanceCore(self, root, max_distance):
        if root.left is None and root.right is None:
            return 0
        leftlen = self.maxDistanceCore(root.left, max_distance)
        rightlen = self.maxDistanceCore(root.right, max_distance)
        val = leftlen + rightlen + 1
        self.max_distance = max(val, self.max_distance)
        return max(leftlen, rightlen) + 1
