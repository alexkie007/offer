import math


def get_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2,2) + math.pow(y1 - y2,2))



print(get_distance(0, 2, 0, 4))
