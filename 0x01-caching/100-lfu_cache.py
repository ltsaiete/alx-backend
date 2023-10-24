#!/usr/bin/env python3
"""
This is a simple module and it only has
one class called MRUCache that inherits from BaseCaching
"""


from base_caching import BaseCaching
from datetime import datetime


class LFUCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.used_items = dict()

    def add_to_used_items(self, key):
        """_summary_

        Args:
            key (_type_): _description_
        """
        if key in self.used_items:
            self.used_items[key] = self.used_items[key] + 1
        else:
            self.used_items[key] = 1

    def discard_item(self):
        """_summary_
        """
        lfu_item = next(iter(self.used_items))

        for k, v in self.used_items.items():
            if v < self.used_items[lfu_item]:
                lfu_item = k

        del self.cache_data[lfu_item]
        del self.used_items[lfu_item]

        print(f'DISCARD: {lfu_item}')

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard_item()

            self.add_to_used_items(key)
            self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key is not None and key in self.cache_data:
            self.add_to_used_items(key)
            return self.cache_data[key]

        return None
