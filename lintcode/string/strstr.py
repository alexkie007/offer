class Solution:
    @staticmethod
    def strstr(source, target):
        if source is None or target is None:
            return -1
        if len(target) == 0:
            return 0
        size = len(target)
        power = 1
        base = pow(10, 6)
        for i in range(size):
            power = power * 31 % base

        targetcode = 0
        for i in range(size):
            targetcode = (targetcode * 31 + ord(target[i])) % base

        hashcode = 0
        for i in range(len(source)):
            hashcode = (hashcode * 31 + ord(source[i])) % base

            if i < size - 1:
                continue
            if i >= size:
                hashcode = (hashcode - ord(source[i - size]) * power) % base
                if hashcode < 0:
                    hashcode += base
            if hashcode == targetcode:
                if source[i - size + 1:i + 1] == target:
                    return i - size + 1
        return -1

s = Solution()
print(s.strstr('abcde','cde'))
