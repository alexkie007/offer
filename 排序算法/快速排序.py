def quickSort(lists):
    if len(lists) <2:
        return lists
    else:
        pivot = lists[0]
        less = [x for x in lists[1:] if x < pivot]
        greater = [x for x in lists[1:] if x > pivot]
        return  quickSort(less)+[pivot]+quickSort(greater)