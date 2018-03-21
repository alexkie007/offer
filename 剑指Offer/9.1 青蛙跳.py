def frogJump(n):
    if n < 1:
        return False
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b, c = 1, 0, 0
    for x in range(n):
        c= a + b
        a, b = b, a+b
    return c

print(frogJump(2))
print(frogJump(3))
print(frogJump(4))
print(frogJump(5))