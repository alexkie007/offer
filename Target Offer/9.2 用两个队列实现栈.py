'''
用两个队列来实现一个栈，完成队列的Push和Pop操作。 队列中的元素为int类型。·
'''


class Solution:
    def __init__(self):
        self.quene1 = []
        self.quene2 = []

    def push(self, x):
        if self.quene2 == []:
            self.quene1.append(x)
        else:
            self.quene2.append(x)

    def pop(self):
        if not self.quene1 and not self.quene2:
            return
        if self.quene1:
            length = len(self.quene1)
            for i in range(length - 1):
                self.quene2.append(self.quene1.pop(0))
            return self.quene1.pop()
        elif self.quene2:
            length = len(self.quene2)
            for i in range(length - 1):
                self.quene1.append(self.quene2.pop(0))
            return self.quene2.pop()
