'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''


class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            temp = self.min()
            self.minstack.append(temp)

    def min(self):
        return self.minstack[-1]

    def pop(self):
        if self.stack == [] or self.minstack == []:
            return None
        self.minstack.pop()
        self.stack.pop()

S = Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())