#!/usr/bin/env python3
""" LIFO Caching """
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ Implements LIFO cache to store and remove items from
    a dictionary if limit is reached.
    """
    def __init__(self):
        """ Initialize the cache. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add item to cache. """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_in, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", last_in)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Retrieve item by key. """
        return self.cache_data.get(key, None)
