def Power(self, base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent == -1:
        return 1 / base
    result = self.Power(base, exponent >> 1)
    result *= result
    if exponent % 2 == 1:
        result *= base
    return result


a = input()
strings = a.split(" ")
n = int(strings[0])
w = int(strings[1])
all = Power(n, w)
ok = n * Power(n - 1, w - 1)
print((all - ok) % 100003)
