#!/usr/bin/env python3
""" 0. Basic dictionary """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache that inherits
    from BaseCaching and is a caching system"""

    def put(self, key, item):
        """ assign to the dictionary
        self.cache_data the item value for the key key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data
        linked to key"""
        return self.cache_data.get(key, None)
