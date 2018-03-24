'''
给定一个字符串，请找出其中无重复字符的最长子字符串。
例如，在”abcabcbb”中，其无重复字符的最长子字符串是”abc”，其长度为 3。
对于，”bbbbb”，其无重复字符的最长子字符串为”b”，长度为1。
'''
class Solution:
    def longestSubstringWithoutDunplcation(self,s):
        res = 0
        if s is None or len(s) ==0:
            return res
        d= {}
        tmp = 0
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] +1
            tmp = i - start +1
            d[s[i]] = i
            res = max(res,tmp)
        return res