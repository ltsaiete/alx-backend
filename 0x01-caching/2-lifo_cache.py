from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.stack[-1]]
                discarded_key = self.stack.pop()
                print(f'DISCARD: {discarded_key}')

            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        if key is not None and self.cache_data.has_key(key):
            return self.cache_data[key]

        return None
