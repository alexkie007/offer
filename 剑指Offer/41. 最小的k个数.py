'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''

def partition(list):
    if len(list) <2:
        return list
    else:
        pivot = list[0]
        less = [x for x in list[1:] if x < pivot]
        greater = [x for x in list[1:] if x > pivot]
        return partition(less)+pivot+partition(greater)


def find_least_k_nums(alist, k):
    length = len(alist)
    if not alist or k <=0 or k > length:
        return None
    partition(alist)
    return alist[:k]

import heapq

def get_least_numers_big_data(list,k):
    max_heap = []
    length = len(list)
    if not list or k <=0 or k >length:
        return
    k = k-1
    for ele in list:
        ele = -ele
        if len(max_heap) <k:
            heapq.heappush(max_heap,ele)
        else:
            heapq.heappushpop(max_heap,ele)

    return map(lambda x: -x ,max_heap)


a = [4,5,1,6,2,7,3,8]
print(get_least_numers_big_data(a,4))


