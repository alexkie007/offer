class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    def rotateString(self, s, offset):
        # write your code here
        size = len(s)
        return self.reverse(self.reverse(s[:size - offset]) + self.reverse(s[size - offset:]))

    def reverse(self, s):
        s = [str(x) for x in s]
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return  "".join(s)


s = Solution()
print(s.rotateString("abcdefg", 3))
