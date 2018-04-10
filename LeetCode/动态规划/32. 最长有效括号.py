"""
给一个只包含 '(' 和 ')' 的字符串，找出最长的有效（正确关闭）括号子串的长度。

对于 "(()"，最长有效括号子串为 "()" ，它的长度是 2。

另一个例子 ")()())"，最长有效括号子串为 "()()"，它的长度是 4。
"""

"""
解题思路：
定义个start变量来记录合法括号串的起始位置，
我们遍历字符串，如果遇到左括号，则将当前下标压入栈，
如果遇到右括号，
    如果当前栈为空，则将下一个坐标位置记录到start，
    如果栈不为空，则将栈顶元素取出，
        此时若栈为空，则更新结果和i - start + 1中的较大值，否
        则更新结果和i - 栈顶元素中的较大值，
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size <= 1:
            return 0
        stack = []
        start = 0
        res = 0
        for i in range(size):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i + 1
                else:
                    stack.pop()
                    res = max(res, i - start + 1) if len(stack) == 0 else max(res, i - stack[-1])

        return res

a=')()())'
s = Solution()
print(s.longestValidParentheses(a))