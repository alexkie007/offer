'''
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
'''


class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == None:
            return s
        hash = {}
        for i in s:
            hash[i] = hash[i] + 1 if hash.get(i) else 1
        for i in s:
            if hash[i] == 1:
                return i
        return None


a = 'googlle'
s = Solution()
print(s.FirstNotRepeatingChar(a))
