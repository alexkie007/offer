"""
求在 逆波兰表示法 中算术表达式的值。

有效的运算符号包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰计数表达。

例如：

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
"""
解题思路：
使用两个栈，一个栈存数字，一个栈中存操作符
然后只要遇到操作符，就取栈中的最后连个元素进行操作，
操作后又放回栈
"""

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stackNumber = []
        stackOperate = []
        for i in tokens:
            try:
                i = int(i)
                stackNumber.append(i)
            except:
                stackOperate.append(i)
                if len(stackNumber) >=2:
                    number0 = str(stackNumber.pop())
                    number1 = str(stackNumber.pop())
                    sum = int(eval(number1+stackOperate.pop()+number0))
                    stackNumber.append(sum)
        return stackNumber.pop()

s = Solution()
# print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
