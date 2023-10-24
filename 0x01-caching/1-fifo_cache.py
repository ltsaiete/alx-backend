from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.queue[0]]
                discarded_key = self.queue.pop(0)
                print(f'DISCARD: {discarded_key}')

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        if key is not None and self.cache_data.has_key(key):
            return self.cache_data[key]

        return None
