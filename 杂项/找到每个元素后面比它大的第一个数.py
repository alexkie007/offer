class Solution:
    def findFirstBig(self, numbers):
        stack = []
        res =[]
        for i in range(len(numbers)):
            while len(stack) != 0 and numbers[i] > stack[-1]:
                res.append()
            stack.append(numbers[i])