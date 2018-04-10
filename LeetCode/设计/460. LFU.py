import collections
class LFUCache(object):
    def __init__(self, capacity):
        self.d = collections.defaultdict(int)
        self.num = collections.defaultdict(collections.OrderedDict)
        self.cap = capacity
        self.min = 1

    def get(self, key):
        if key not in self.d:
            return -1
        value = self.num[self.d[key]][key]
        self.update(key, value)
        return value

    def put(self, key, value):
        self.update(key, value)

    def update(self, key, value):
        count = self.d[key]
        self.d[key] = count + 1
        if count: self.num[count].pop(key)
        self.num[count + 1][key] = value
        if len(self.d) > self.cap:
            first, _ = self.num[self.min].popitem(last=False)
            self.d.pop(first)
        if count == self.min and not self.num[count]:
            self.min = count + 1
        else:
            self.min = min(self.min, count + 1)

cache = LFUCache(3)
cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3,3)
cache.put(4,4)