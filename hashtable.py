'''
hash table using a naive hash function, implemented using linked lists.
it is designed to be functionally identical to python's built-in dict data structure
'''
from buckets import Bucket, BucketHolder, NoBucket

SIZE = 256


class HashTable:
    def __init__(self, size=SIZE):
        self.buckets = BucketHolder()
        self.size = size

    def get(self, key, default=None):
        hashed_key = self._naive_hash(key)
        try:
            bucket = self.buckets.get(hashed_key)
            out = bucket.get(key)
        except KeyError:
            return default
        return out

    def items(self):
        for bucket_node in self.buckets:
            bucket = bucket_node.value
            for node in bucket:
                yield (node.key, node.value)

    def keys(self):
        for key, _ in self.items():
            yield key

    def values(self):
        for _, value in self.items():
            yield value

    def _naive_hash(self, key):
        return sum((ord(c) ** i) for i, c in enumerate(str(key), 1)) % self.size

    def __setitem__(self, key, value):
        hashed_key = self._naive_hash(key)
        try:
            bucket = self.buckets.get(hashed_key)
            if key in bucket:
                bucket.remove(key)
            bucket.push(key, value)
        except NoBucket:
            new_bucket = Bucket(bucket_id=hashed_key)
            new_bucket.push(key, value)
            self.buckets.push(new_bucket)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        hashed_key = self._naive_hash(key)
        try:
            bucket = self.buckets.get(hashed_key)
        except (KeyError, NoBucket):
            raise KeyError(key)
        bucket.remove(key)

    def __contains__(self, key):
        hashed_key = self._naive_hash(key)
        try:
            bucket = self.buckets.get(hashed_key)
        except NoBucket:
            return False
        return key in bucket

    def __bool__(self):
        return bool(self.buckets)

    def __len__(self):
        i = 0
        for bucket_node in self.buckets:
            bucket = bucket_node.value
            i += len(bucket)
        return i

    def __iter__(self):
        for bucket_node in self.buckets:
            bucket = bucket_node.value
            for node in bucket:
                yield node.key

    def __repr__(self):
        output = '{'
        for bucket_node in self.buckets:
            bucket = bucket_node.value
            for node in bucket:
                output += '%r: %r, ' % (node.key, node.value)
        output = output[:-2]
        output += '}'
        return output
