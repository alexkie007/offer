class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        if x[:] == x[::-1]:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(12321))
    print(s.isPalindrome(0))
    print(s.isPalindrome(-1))