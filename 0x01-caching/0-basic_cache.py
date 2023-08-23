#!/usr/bin/env python3
""" Basic dictionary """
from base_caching import BaseCaching
# BasicCaching = __import__("Base_caching").BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)
