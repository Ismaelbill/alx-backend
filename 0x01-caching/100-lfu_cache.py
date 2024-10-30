#!/usr/bin/env python3
""" 5. LFU Caching """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching
LRUCache = __import__('3-lru_cache').LRUCache


class LFUCache(BaseCaching):
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

        while len(obj) > BaseCaching.MAX_ITEMS:
            LRUCache.put(self, key, item)

    def get(self, key):
        """ return the value in self.cache_data
        linked to key"""
        obj = self.cache_data
        if key and key in obj:
            item = obj.pop(key)
            obj[key] = item
        return self.cache_data.get(key, None)
