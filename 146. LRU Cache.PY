from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if key in self.cache:
            # if we access an item from cache we need to add it to end of cache dict
            val = self.cache.pop(key)
            self.cache[key]=val
            return val
        return -1
        

    def put(self, key: int, value: int) -> None:
        #remove element to replace with new val
        if key in self.cache:
            self.cache.pop(key)
        else:
            # if capacity exceeds pop a key-val 
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        
        # at the end we could add to cache
        self.cache[key] = value
        
