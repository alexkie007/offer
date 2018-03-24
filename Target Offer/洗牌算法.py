#
import random
# 每次从剩下的牌中取一个
def shuffle(lis):
    result = []
    while lis:
        p = random.randrange(0, len(lis))
        result.append(lis[p])
        lis.pop(p)
    return result

# 每次从未处理的数据中随机取出一个数字，然后把该数字放在数组的尾部，即数组尾部存放的是已经处理过的数字。
def shuffle2(lis):
    for i in range(len(lis) - 1, 0, -1):
        p = random.randrange(0, i + 1)
        lis[i], lis[p] = lis[p], lis[i]
    return lis



def shuffle3(lis):
    result = lis[:]
    for i in range(1, len(lis)):
        j = random.randrange(0, i)
        result[i] = result[j]
        result[j] = lis[i]
    return result