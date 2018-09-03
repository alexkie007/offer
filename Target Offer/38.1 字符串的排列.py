'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''


class Solution:
    def Permutation(self, ss):
        if ss == None or len(ss) < 2:
            return ss
        result = []
        length = len(ss)
        charList = list(ss)
        charList.sort()
        for i in range(length):
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            temp = self.Permutation(''.join(charList[:i]) + ''.join(charList[i + 1:]))
            for j in temp:
                result.append(charList[i] + j)

        return result


ss = 'acb'
S = Solution()
a = S.Permutation(ss)
a = ",".join(a)
import sys

sys.stdout.write(a)
