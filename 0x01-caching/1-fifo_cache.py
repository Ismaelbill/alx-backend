#!/usr/bin/env python3
"""  1 .FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """  inherits from BaseCaching and
         is a caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary
        self.cache_data the item value for the key key"""
        obj = self.cache_data
        if key and item:
            obj[key] = item
        if len(obj) > BaseCaching.MAX_ITEMS:
            x = list(obj.keys())[0]
            del obj[x]
            print('DISCARD: {}'.format(x))

    def get(self, key):
        """ return the value in self.cache_data
        linked to key"""
        return self.cache_data.get(key, None)
