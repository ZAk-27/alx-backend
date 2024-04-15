#!/usr/bin/python3
""" module """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ module"""

    def put(self, key, item):
        """module"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """module"""
        return self.cache_data.get(key)
