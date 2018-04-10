"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字串中增加空格来构建一个句子，使得句子里所有的单词都在词典中。你可以假设字典中无重复的单词。

返回所有这些可能的句子。

例如，给出
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

答案为 ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):

wordDict 参数已被更改为字符串列表（而不是一组字符串）。请重新加载代码定义以获取最新更改。
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.wordBreakCore(s, wordDict, {})

    def wordBreakCore(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s: return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfRest = self.wordBreakCore(s[len(word):], wordDict, memo)
                for item in resultOfRest:
                    item = word + ' '+ item
                    res.append(item)
        memo[s] = res
        return res
