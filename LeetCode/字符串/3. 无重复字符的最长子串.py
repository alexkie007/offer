"""
给定一个字符串，找出不含有重复字符的 最长子串 的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列 而不是子串。
"""
"""
解题思路：
初始化一个dict， 其中key是字符，value值当前字符最后出现一次的位置
遍历字符串，如果当前字符已经出现过且最后一次出现的位置大于start，则更改start值
然后计算当前最长长度

"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        start = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]]+1
            d[s[i]] = i
            curLen = i - start + 1
            maxLen = max(curLen, maxLen)
        return maxLen

s = Solution()
# print(s.lengthOfLongestSubstring('bbbbb'))
# print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring('dvdf'))