'''
请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''


class Solution:

    # def replaceSpace(self, s):
    #     """
    #     :param s: 源字符串
    #     :return:  修改字符后的字符串
    #     """
    #     return s.replace(' ', '%20')

    def replaceSpace2(self, s):
        """
        :param s: 源字符串
        :return:  修改字符后的字符串
        """
        if not isinstance(s, str) or len(s) <= 0 or s == None:
            return ""
        originalLength = len(s)
        numberofBlank = 0
        for i in range(len(s)):
            if s[i] == ' ':
                numberofBlank += 1
        newLength = originalLength + numberofBlank * 2
        p2 = newLength - 1
        p1 = originalLength - 1
        s2 = [" "] * newLength
        while p1 >= 0 and p2 >= p1:
            if s[p1] == ' ':
                s2[p2 - 2:p2 + 1] = ['%', '2', '0']
                p2 -= 3
            else:
                s2[p2] = s[p1]
                p2 -= 1
            p1 -= 1
        return "".join(s2)

    def replaceSpace3(self, s):
        string = list(s)
        stringReplace = []
        for item in string:
            if item == ' ':
                stringReplace.append('%')
                stringReplace.append('2')
                stringReplace.append('0')
            else:
                stringReplace.append(item)
        return "".join(stringReplace)


s = Solution()
s1 = str("hello world")
print(s.replaceSpace2(s1))
