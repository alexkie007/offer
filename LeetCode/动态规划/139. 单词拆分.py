"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，确定 s 是否可以被空格分割为一个或多个在字典里出现的单词。你可以假设字典中无重复的单词。

例如，给出
s = "leetcode"，
dict = ["leet", "code"]。

返回 true 因为 "leetcode" 可以被切分成 "leet code"。
"""
"""
d is an array that contains booleans

d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

s = “leetcode”

words = [“leet”, “code”]

d[3] is True because there is “leet” in the dictionary that ends at 3rd index of “leetcode”

d[7] is True because there is “code” in the dictionary that ends at the 7th index of “leetcode” AND d[3] is True
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        res = [False] * (len(s)+1)
        res[0] = True
        for i in range(1, len(s)+1):
            for w in wordDict:
                if res[i-len(w)] and w == s[i-len(w):i] :
                    res[i] = True
        return res[-1]


a = 'leetcode'
a1 = 'aaaaaaa'
word = ['leet', 'code']
word1 = ['aaaa', 'aa']
s = Solution()
print(s.wordBreak(a1, word1))



