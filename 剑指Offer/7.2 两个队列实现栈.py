class Solution:
    def __init__(self):
        self.quene1 = []
        self.quene2 = []

    def push(self,x):
        if self.quene2 == []:
            self.quene1.append(x)
        else:
            self.quene2.append(x)

    def pop(self):
        if not self.quene1 and not self.quene2:
            return
        if self.quene1:
            length = len(self.quene1)
            for i in range(length-1):
                self.quene2.append(self.quene1.pop(0))
            return self.quene1.pop()
        elif self.quene2:
            length = len(self.quene2)
            for i in range(length-1):
                self.quene1.append(self.quene2.pop(0))
            return self.quene2.pop()

P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())