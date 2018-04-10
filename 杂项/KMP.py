
class Solution:
    # 首先找到转移表 然后再进行运算， 这样时间复杂度就可以为o(M+N)
    def partialTable(self, s):
        prefix = [s[:i + 1] for i in range(len(s) - 1)]
        postfix = [s[i + 1:] for i in range(len(s) - 1)]
        intersection = list(set(prefix) & set(postfix))
        if intersection:
            return len(intersection[0])
        return 0

    def kmp(self, s, c):
        i = 0
        ret = []
        while i<len(s) -len(c)+1:
            match = True
            for j in range(len(c)):
                if s[i+j] != c[j]:
                    match = False
                    break
            if match:
                ret.append(i)
                i += len(c)
            else:
                i += max(j - self.partialTable(c[:j]), 1)

        return ret

s = Solution()
a = "bacbababadababacambabacaddababacasdsd"
b = 'ababaca'
print(s.kmp(a,b))

