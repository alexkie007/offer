'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''


class Solution:
    def group(self, ss):
        if ss == None or len(ss) < 2:
            return ss
        result = []
        length = len(ss)
        charList = list(ss)
        charList.sort()
        for i in range(length):
            result.append(charList[i])
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            temp = self.group(''.join(charList[i + 1:]))
            for j in temp:
                result.append(charList[i] + j)
        return result


ss = 'acb'
S = Solution()
print(S.group(ss))
