'''
编写一个类，用两个栈实现队列，支持队列的基本操作(add, poll, peek)。
'''

class Solution:
    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    def add(self, val):
        self.stackPush.append(val)

    def poll(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("Queue is Empty")
        elif not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()

    def peek(self):
        if not self.stackPush and not self.stackPop:
            raise Exception("Queue is Empty")
        elif not self.stackPop:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        return self.stackPop.pop()
