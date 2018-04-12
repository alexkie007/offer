"""

设计和实现一个  LRU（最近最少使用）缓存 数据结构，使它应该支持以下操作： get 和 put 。

get(key) - 如果密钥存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
put(key, value) - 如果密钥不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前使最近最少使用的项目作废。

后续:

你是否可以在 O(1) 时间复杂度中进行两种操作？

案例:

LRUCache cache = new LRUCache( 2 /* 容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作，会将 key 2 作废
cache.get(2);       // 返回 -1 (结果不存在)
cache.put(4, 4);    // 该操作，会将 key 1 作废
cache.get(1);       // 返回 -1 (结果不存在)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
"""

import collections
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        v = self.dict.pop(key)
        self.dict[key] = v
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.remain > 0:
                self.remain -=1
            else:
                self.dict.popitem(last=False)
        self.dict[key] = value
cache = LRUCache(3)
cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3,3)
cache.put(4,4)