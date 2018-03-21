def cut_rope(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    timesOf3 = length//3
    if (length - timesOf3 *3 ==1):
        timesOf3 -=1

    timesOf2 = (length - timesOf3 *3)/2

    return 3*timesOf3 * 2*timesOf2

print(cut_rope(5))
