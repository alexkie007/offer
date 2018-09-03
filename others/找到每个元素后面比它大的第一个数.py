"""

解题思路：
1. 栈里面保留是索引，而非元素，其实这是一个很关键的地方，索引的信息要比内容多，因为可以索引本身就可以确定内容。要牢记这一特点

2、初始栈，里面为第一个元素

3、如果栈不为空，而且当前处理元素比栈顶元素大，则栈顶元素对应的第一个比它大的值，就是该元素

4、弹出栈顶元素，继续处理栈里的元素，直至为空或当前处理元素不大于栈顶元素

5、将当前元素压入栈
"""


class Solution:
    def findFirstBig(self, numbers):
        stack = []
        res = [-1] * len(numbers)
        stack.append(0)
        for i in range(1, len(numbers)):
            while len(stack) > 0 and numbers[i] > numbers[stack[-1]]:
                res[stack[-1]] = numbers[i]
                stack.pop()
            stack.append(i)
        return res

    def findFirstSmall(self, numbers):
        stack = []
        res = [-1] * len(numbers)
        stack.append(0)
        for i in range(1, len(numbers)):
            while len(stack) > 0 and numbers[i] < numbers[stack[-1]]:
                res[stack[-1]] = numbers[i]
                stack.pop()
            stack.append(i)
        return res


s = Solution()
print(s.findFirstBig([3, 2, 4, 1, 6]))
print(s.findFirstSmall([3, 2, 4, 1, 6]))
