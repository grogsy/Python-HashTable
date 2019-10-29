from linkedlist import LinkedList
from nodes import HashNode


class NoBucket(KeyError):
    pass


class BucketHolder(LinkedList):
    '''A linked-list that holds other linked-lists(buckets)'''

    def _get_id(self, bucket_id):
        for bucket_node in self:
            bucket = bucket_node.value
            if bucket.id == bucket_id:
                return bucket
        return None

    def get(self, bucket_id):
        bucket = self._get_id(bucket_id)
        if not bucket:
            raise NoBucket
        return bucket


class Bucket(LinkedList):
    def __init__(self, bucket_id=None):
        super().__init__()
        self.id = bucket_id
        self._node = HashNode

    def _init_insert(self, key, value):
        self.head = self.tail = self._node(key=key, value=value, prev=None, nxt=None)

    def push(self, key, value):
        if not self.head:
            self._init_insert(key, value)
        else:
            self.tail = self._node(key=key, value=value, prev=self.tail, nxt=None)
            self.tail.prev.next = self.tail

    def get(self, key):
        for node in self:
            if node.key == key:
                return node.value
        raise KeyError(key)

    def remove(self, key):
        for node in self:
            if node.key == key:
                if node is self.head:
                    self.unshift()
                elif node is self.tail:
                    self.pop()
                else:
                    prev_node, next_node = node.prev, node.next
                    prev_node.next, next_node.prev = next_node, prev_node
                break
        return None

    def __contains__(self, key):
        for node in self:
            if key == node.key:
                return True
        return False
