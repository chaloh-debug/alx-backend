#!/usr/bin/env python3
""" FIFO Caching """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ Implement FIFO cache to store and remove items from
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
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_in, _ = self.cache_data.popitem(last=False)
            print("DISCARD", first_in)

    def get(self, key):
        """ Retrieve item by key. """
        return self.cache_data.get(key, None)
