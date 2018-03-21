'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''


def NumberOf1Between1AndN(n):
    ones ,m = 0,1
    while m<n:
        ones += (n//m % 10 ==1) * ( n % m + 1) + (n//m  +8) //10 *m
        m *=10
    return ones

print(NumberOf1Between1AndN(526))