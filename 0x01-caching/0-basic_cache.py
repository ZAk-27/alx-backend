#!/usr/bin/python3
"""Basic Caching  implement
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching implement

    Attributes:
        MAX_ITEMS: number of items that can be store in the cache
    """
    def put(self, key, item):
        """ Add item in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item 
        """
        return self.cache_data.get(key, None)
