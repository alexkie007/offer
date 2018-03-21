



def singleton(cls, *args, **kargs):
    instance = {}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kargs)
        return instance[cls]
    return getinstance()

@singleton()
class Myclass:
    a = 1
    def __init__(self, x):
        self.x = x

