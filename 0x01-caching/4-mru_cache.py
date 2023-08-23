#!/usr/bin/env python3
""" MRU Caching """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Implements MRU cache to store and remove items from
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
            if len(self.cache_data) + 1 >  BaseCaching.MAX_ITEMS:
                most_ru, _ = self.cache_data.popitem(False)
                print("DISCARD", most_ru)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key. """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
