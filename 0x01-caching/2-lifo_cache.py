#!/usr/bin/env python3
"""
This is a simple module and it only has
one class called LIFOCache that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """
    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.stack[-1]]
                discarded_key = self.stack.pop()
                print(f'DISCARD: {discarded_key}')

            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key is not None and self.cache_data.has_key(key):
            return self.cache_data[key]

        return None
