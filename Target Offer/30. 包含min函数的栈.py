'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''

# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)
        if len(self.stack2) == 0:
            self.stack2.append(node)
        elif node < self.stack2[-1]:
            self.stack2.append(node)
        else:
            self.stack2.append(self.stack2[-1])

        # write code here
    def pop(self):
        if self.stack1 ==None:
            return None
        self.stack2.pop()
        return self.stack1.pop()

        # write code here
    def top(self):
        return self.stack1[-1]


        # write code here
    def min(self):
        return self.stack2[-1]
        # write code here

s = Solution()
s.push(3)
s.min()
s.push(4)
s.min()
s.push(2)
s.min()
s.push(3)
s.min()
s.pop()
s.min()
s.pop()
s.min()
s.pop()
s.min()
s.push(0)
print(s.min())