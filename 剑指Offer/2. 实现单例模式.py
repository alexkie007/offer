# class Singleton():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_instance'):
#             orig = super(Singleton,cls)
#             cls._instance = orig.__new__(cls, *args, **kwargs)
#         return cls._instance
#
# class MyClass(Singleton):
#     a = 1


def singleton(cls, *args, **kwargs):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class MyClass(object):
    a = 1
    def __init__(self, x = 0):
        self.x = x


one = MyClass()
two = MyClass()
two.a = 3
print(one.a)            # 3
print(id(one))          # 8842576
print(id(two))          # 8842576
print(one == two)       # True
print(one is two)       # True
one.x = 1
print(one.x)            # 1
print(two.x)