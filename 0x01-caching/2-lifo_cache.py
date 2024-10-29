#!/usr/bin/env python3
""" 2. LIFO Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
        if key in obj:
            del obj[key]
        if len(obj) >= BaseCaching.MAX_ITEMS:
            x = list(obj.keys())[-1]
            del obj[x]
            print('DISCARD: {}'.format(x))
        if key and item:
            obj[key] = item

    def get(self, key):
        """ return the value in self.cache_data
        linked to key"""
        return self.cache_data.get(key, None)
