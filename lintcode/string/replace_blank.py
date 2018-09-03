class Solution:
    @staticmethod
    def replace_blank(s):
        origin_size = len(s)
        number_of_blank = 0
        for i in s:
            if i == " ":
                number_of_blank += 1
        new_size = origin_size + 2 * number_of_blank
        p2 = new_size - 1
        p1 = origin_size - 1
        s2 = [" " for i in range(new_size)]
        while p1 >= 0 and p2 >= p1:
            if s[p1] == " ":
                s2[p2 - 2:p2 + 1] = ["%", "2", '0']
                p2 -= 3
            else:
                s2[p2] = s[p1]
                p2 -= 1
            p1 -= 1
        return "".join(s2)

s = Solution()
print(s.replace_blank("hello world"))
