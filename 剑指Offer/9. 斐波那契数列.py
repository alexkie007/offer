class Solution:
    def fib(self, n):
        if n < 0:
            return False
        result  = [0, 1]
        if n < 2:
            return result[n]
        a, b, result = 1, 0, 0

        for i in range(n):
            result = a+b
            a, b = b, a+b
        return result

test = Solution()


print(test.fib(0))
print(test.fib(1))
print(test.fib(2))
print(test.fib(3))
print(test.fib(4))