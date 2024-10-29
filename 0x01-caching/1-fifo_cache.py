#!/usr/bin/env python3
"""  1 .FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """  """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary
        self.cache_data the item value for the key key"""
        if key and item:
            obj = self.cache_data
            obj[key] = item
        if len(obj) > BaseCaching.MAX_ITEMS:
            x = list(obj.keys())[0]
            print('DISCARD: {}'.format(x))
            del obj[x]

    def get(self, key):
        """ return the value in self.cache_data
        linked to key"""
        return self.cache_data.get(key, None)
