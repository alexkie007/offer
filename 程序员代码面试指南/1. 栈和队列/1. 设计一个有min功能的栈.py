'''
实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作

1、 pop、push、getMin操作的时间复杂度都是O(1)。
2.、设计的栈类型可以使用现成的栈结构
'''

class Solution:
    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, val):
        self.stackData.append(val)
        if  len(self.stackMin) == 0 or self.stackMin[-1]>val:
            self.stackMin.append(val)
        else:
            self.stackMin.append(self.min())

    def pop(self):
        if len(self.stackData) <1:
            raise Exception("Stack is Empty")
        else:
            self.stackMin.pop()
            return self.stackData.pop()


    def min(self):
        if len(self.stackMin) ==0:
            raise Exception("Stack is Empty")
        return self.stackMin[-1]