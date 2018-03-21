def find_integer(martix,num):
    """

    :param martix:
    :param num:
    :return:
    """
    if not martix:
        return False
    rows, cols = len(martix), len(martix[0])
    row, col = rows - 1, 0
    while row >=0 and col <=cols -1:
        if martix[row][col] == num:
            print(row,col)
            return True
        elif martix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False

import numpy as np
array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]

print(find_integer(array, 4))