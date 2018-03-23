def shellSort(lists):
    count = len(lists)
    step =2
    group = int(count/step)
    while group>0:
        for i in range(group):
            j = i+group
            while j<count:
                k = j-group
                
