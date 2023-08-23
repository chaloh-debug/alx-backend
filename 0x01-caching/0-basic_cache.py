#!/usr/bin/env python3
""" Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Implements basic objects to store and retrieve a dictionary. """
    def put(self, key, item):
        """ Store item to a dictioary. """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item by key. """
        return self.cache_data.get(key, None)
