'''
一个栈中元素的类型是整型，现在想将该栈从顶到底按从大到小的顺序排序，
只许申请一个栈。除此之外，可以申请新的变量，但不能申请额外的数据结构。如何完成排序？
'''
'''
不断将栈顶元素cur弹出，
    如果新栈为空、或者新栈栈顶元素大于cur，直接将cur压入新栈中；
    否则，将新栈中的元素逐一弹出压回原来的栈中，
    直到新栈的栈顶元素大于cur，再将cur压入新栈中.
    继续弹出原来栈的栈顶元素，重复上述操作即可
'''


class Solution:
    def sortByStack(self, stack):
        if len(stack) < 2:
            return stack
        stack1 = []
        while stack:
            cur = stack.pop()
            while len(stack1) != 0 and stack1[-1] < cur:
                stack.append(stack1.pop())
            stack1.append(cur)
        while stack1:
            stack.append(stack1.pop())
        return stack
