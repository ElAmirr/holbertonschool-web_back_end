#!/usr/bin/env python3
""" LRUCache module """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache class inherits from BaseCaching """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache using LRU """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = next(iter(self.cache_data))
                print(f"DISCARD: {lru_key}")
                self.cache_data.pop(lru_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key, None)
