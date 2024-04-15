#!/usr/bin/env python3
"""module.
"""


class BaseCaching():
    """module.
    """
    MAX_ITEMS = 4

    def __init__(self):
        """module.
        """
        self.cache_data = {}

    def print_cache(self):
        """module.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """module.
        """
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        """module.
        """
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)
