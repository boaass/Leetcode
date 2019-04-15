# -*- coding:utf-8 -*-

# Design a HashMap without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap,
# update the value. get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no
# mapping for the key. remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

# Note:
#
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.initCapacity = 4 * 1024    # 初始容量
        self.loadFactor = 0.75  # 负载因子
        self.curCapacity = self.initCapacity    # 当前容量
        self.elementCount = 0   # 当前元素数量
        self.hashMap = [[] for _ in range(self.curCapacity)]

    def custom_hash(self, key):
        """
        :type key: int
        :return: int
        """
        return key % self.curCapacity

    def reHash(self):
        if self.elementCount / self.curCapacity >= self.loadFactor:
            self.curCapacity *= 2
        else:
            if self.curCapacity is not self.initCapacity:
                self.curCapacity //= 2
            else:
                return

        t_hashMap = [t for t in self.hashMap]
        self.hashMap = [[] for _ in range(self.curCapacity)]
        for t in t_hashMap:
            for k, v in t:
                self.put(k, v)

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """

        self.remove(key)

        self.elementCount += 1
        t = self.hashMap[self.custom_hash(key)]
        t.append((key, value))

        self.reHash()

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        t = self.hashMap[self.custom_hash(key)]
        for k, v in t:
            if k == key:
                return v

        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        t = self.hashMap[self.custom_hash(key)]
        old_t = None
        for k, v in t:
            if k == key:
                old_t = (key, v)
                break
        if old_t:
            self.elementCount -= 1
            t.remove(old_t)

        self.reHash()


if __name__ == '__main__':
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    print hashMap.get(1)              # returns 1
    print hashMap.get(3)              # returns -1 (not found)
    hashMap.put(2, 1)           # update the existing value
    print hashMap.get(2)              # returns 1
    hashMap.remove(2)           # remove the mapping for 2
    print hashMap.get(2)              # returns -1 (not found)