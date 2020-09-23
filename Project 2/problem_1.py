from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity=5):
        if capacity < 1:
            raise ValueError("Capacity cannot less than 1")
        self.capacity = capacity
        self.cache = OrderedDict()
        # Initialize class variables

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        value = -1
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key is None:
            print("Key cannot be None. The data will not be added")
            return
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            cache_size = len(self.cache)
            if self.capacity > 0:
                if cache_size < self.capacity:
                    self.cache[key] = value
                else:
                    self.cache.popitem(False)
                    self.cache[key] = value


if __name__ == "__main__":
    # Udacity test case
    our_cache = LRUCache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)

    our_cache.set(6, 6)

    print(
        our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    # Test 1
    print("Test 1")
    our_cache = LRUCache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(1))  # return -1 because  (1,1) is evicted due to over capacity
    print(our_cache.cache)  # return [(2,2), (3,3), (4,4), (5,5), (6,6)]

    # Test 2
    print("Test 2")
    our_cache = LRUCache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(None, None)  # do nothing and print Key cannot be None. The data won't be added
    our_cache.set(3, None)

    print(our_cache.cache)  # [(1, 1), (2, 2), (3, None)]

    # Test 3
    print("Test 3")
    our_cache = LRUCache(0)  # raise ValueError Capacity cannot less than 1
