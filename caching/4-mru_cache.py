#!/usr/bin/env python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class inherits from BaseCaching """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """ Add an item in the cache using MRU """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.mru_key}")
                self.cache_data.pop(self.mru_key)
            self.cache_data[key] = item
            self.mru_key = key

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.mru_key = key
        return self.cache_data.get(key, None)
