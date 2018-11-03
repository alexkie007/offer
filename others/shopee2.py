class point():  # 定义类
    def __init__(self, x, y):
        self.x = x
        self.y = y


def mult(a,b, c):
    return (a.x-c.x)*(b.y-c.y)-(b.x-c.x)*(a.y-c.y)


def IsIntersec(p1, p2, p3, p4):  # 判断两线段是否相交
    if (max(p1.x, p2.x) < min(p3.x, p4.x)):
        return "false"
    if (max(p1.y, p2.y) < min(p3.y, p4.y)):
        return "false"
    if (max(p3.x, p4.x) < min(p1.x, p2.x)):
        return "false"
    if (max(p3.y, p4.y) < min(p1.y, p2.y)):
        return "false"
    if (mult(p3, p2, p1) * mult(p2, p4, p1) < 0):
        return "false"
    if (mult(p1, p4, p3) * mult(p4, p2, p3) < 0):
        return "false"
    return "true"

dots = [int(x) for x in input().split(" ") ]
p1 = point(dots[0], dots[1])
p2 = point(dots[2], dots[3])
p3 = point(dots[4], dots[5])
p4 = point(dots[6], dots[7])
print(IsIntersec(p1,p2,p3,p4))
