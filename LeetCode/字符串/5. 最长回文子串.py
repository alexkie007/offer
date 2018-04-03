"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 长度最长为1000。

示例:

输入: "babad"

输出: "bab"

注意: "aba"也是有效答案


示例:

输入: "cbbd"

输出: "bb"
"""
"""
解题思路：
主要分为两种情况，如示例所示，回文长度为奇数和偶数，
我们只需从任意一个节点出发，往两边走，看两边的字符是否相等
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        length  = len(s)
        for i in range(length):
            tmp = self.helper(s, i, i)
            if len(tmp) >len(res):
                res = tmp
            tmp = self.helper(s, i, i+1)
            if len(tmp) >len(res):
                res = tmp
        return res

    def helper(self,s ,l, r):
        while l >= 0 and r <len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

s = Solution()
print(s.longestPalindrome("babad"))