#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching :
      - constants of  caching system
      -  data where stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliazing
        """
        self.cache_data = {}

    def print_cache(self):
        """ Printing cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Adding an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Geting an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
