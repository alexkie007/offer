
"""
把一个整数减去1，再和原整数做与运算，就会把整数最右边的1变成0
"""
def num_of_1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n-1
    return ret

print(num_of_1(6))