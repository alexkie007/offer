def selectSort(lists):
    count = len(lists)
    for i in range(count):
        min = i
        for j in range(i+1,count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i] , lists[min]
    return lists

