#!/usr/bin/env python3
""" 3. LRU Caching """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """  inherits from BaseCaching and
         is a caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ assign to the dictionary
        self.cache_data the item value for the key key"""
        obj = self.cache_data
        if not (key and item):
            return

        if key in obj:
            del obj[key]
        obj[key] = item

        if len(obj) > BaseCaching.MAX_ITEMS:
            x, _ = obj.popitem(last=False)
            print('DISCARD: {}'.format(x))

    def get(self, key):
        """ return the value in self.cache_data
        linked to key"""
        obj = self.cache_data
        if key and key in obj:
            item = obj.pop(key)
            obj[key] = item
        return self.cache_data.get(key, None)
