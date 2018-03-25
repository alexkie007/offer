'''
一个栈依次压入1、2、3、4、5，那么从栈顶到栈底分别为5、4、3、2、1。
将这个栈转置后，从栈顶到栈底为1、2、3、4、5，也就是实现栈中元素的逆序，
但是只能用递归函数实现，不能使用其他数据结构。
'''
'''
解决思路
　　首先实现一个递归函数 a，其功能是返回并移除栈底元素。
    之后再实现一个递归函数 b，其功能是不断用递归的临时变量去接住 a 函数返回的栈底元素，
    这样，最后一个栈底元素就是原来栈的栈顶元素，
    之后一层一层的将递归中的临时变量压入栈中，这样就实现了逆序。
'''
class Solution:



    def getAndRemoveLastElement(self, stack):
        result =  stack.pop()
        if len(stack) ==  0:
            return result
        else:
            i  = self.getAndRemoveLastElement(stack)
            stack.append(result)
            return i

    def reverse(self,stack):
        if len(stack) ==0:
            return
        i = self.getAndRemoveLastElement(stack)
        self.reverse(stack)
        stack.append(i)
        return stack
