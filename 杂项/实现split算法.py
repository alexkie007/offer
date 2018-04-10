class Solution:
    def spilt(self, string, c):
        res = []
        now = ""
        for i in string:
            if i == c:
                res.append(now)
                now = ""
            else:
                now +=i
        res.append(now)
        return res

a = 'asdasdasd'
s = Solution()
print(s.spilt(a,'a'))
