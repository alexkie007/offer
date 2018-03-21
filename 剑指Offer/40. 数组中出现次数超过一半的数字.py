'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

def getMoreHalfNumber(num):
    hash = dict()
    length = len(num)
    for n in num:
        hash[n] = hash[n] + 1 if hash.get(n) else 1
        if hash[n] > length/2:
            return n


a = [1,2,3,2,2,2,5,4,2,3,3,3]
print(getMoreHalfNumber(a))
